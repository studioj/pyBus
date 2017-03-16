#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Use of python-mpd2 for better documentation.
import pprint, os, sys, time, signal, logging
from mpd import (MPDClient, CommandError)
from socket import error as SocketError
import pyBus_core as core
from tinytag import TinyTag

# TODO add long push and short push to add functions
# TODO Beware of the path of the files
# TODO Add the timer to come back to the original display of the song.
# TODO defind other displaytyle to browse via Artists, and on on
# TODO Define a info Mode to display titles/time, artist...

#####################################
# GLOBALS
#####################################
HOST     = 'localhost'
PORT     = '6600'
PASSWORD = False
CON_ID   = {'host':HOST, 'port':PORT}
VOLUME   = 90

CLIENT   = None
T_STATUS = None

rootDir     = '/home/pi/Music'
displayDir  = 'hello'

# Choose to display when browsing : artist /title / (following TinyTag)
displaytype = 'title'

#####################################
# FUNCTIONS
#####################################
def mpdConnect(client, con_id):
  try:
    client.connect(**con_id)
  except SocketError:
    return False
  return True

def init():
  global CLIENT
  ## MPD object instance
  CLIENT = MPDClient()
  if mpdConnect(CLIENT, CON_ID):
    logging.info('Connected to MPD server')
    #CLIENT.setvol(100)

    repeat(True) # Repeat all tracks
  else:
    logging.critical('Failed to connect to MPD server')
    logging.critical("Sleeping 1 second and retrying")
    time.sleep(1)
    init()

# Updates MPD library
def update():
  logging.info('Updating MPD Library')
  CLIENT.update()

def quit():
  if CLIENT:
    CLIENT.disconnect()

def playpause():
  status = CLIENT.status()
  if (status['state']=='play'):
      CLIENT.pause()
      return "Pause"
  elif (status['state']=='stop' or status['state']=='pause'):
      CLIENT.play()
      return client.currentsong()['title']

def stop():
  if CLIENT:
    CLIENT.stop()
    return 'Stopped'

def volumeUp():
    status = CLIENT.status()
    volume = int(status['volume'])
    if (volume < 95):
        volume += 5
        return "Vol "+ str(volume)
    else :
        volume = 100
        return "Vol max"
    CLIENT.setvol(volume)

def volumeDown():
    status = CLIENT.status()
    volume = int(status['volume'])
    if (volume > 5):
        volume -= 5
        return "Vol "+ str(volume)
    else :
        volume = 0
        return "Vol off"
    CLIENT.setvol(volume)

def next():
  CLIENT.next()
  return CLIENT.currentsong()['title']

def previous():
  CLIENT.previous()
  return CLIENT.currentsong()['title']

def next_element(currentElement, up) :
 	try :
 		(_, dirnames, filenames) = iter(os.walk(os.path.dirname(currentElement))).next()
 		dirnames.sort()
 		filenames.sort()
 		listElements = dirnames + filenames
 	except StopIteration:
 		# If directory to walk on does not exists :
 		listElements = currentElement

 	# Remove hidden elements (start with .)
 	listElements = [x for x in listElements if not x.startswith('.')]

 	# Find the index in the list of the displayed name.
 	(basepath, elementName) = os.path.split(currentElement)
 	indexInList = listElements.index(elementName)

 	# Set the way to parse the list.
 	if not up :
 		if indexInList != len(listElements) -1 :
 			nextElement = listElements[indexInList+1]
 		else :
 			nextElement = listElements[0]
 	else :
 		if indexInList != 0 :
 			nextElement = listElements[indexInList-1]
 		else :
 			nextElement = listElements[-1]

 	return os.path.join(basepath, nextElement)

def plus() :
    global displayDir
    if displayDir != rootDir :
        displayDir = next_element(displayDir, 0)
    #print displayDir
    if displayDir.endswith('.mp3') :
        # Display the artist ID3 tag of the next song.
        tag = TinyTag.get(displayDir)
        if tag.title :
            return tag.title	#getattr(self,displaytype)
        else :
            return os.path.basename(displayDir)
    else :
        #(_, toScreen )= os.path.split(displayDir)
        return os.path.split(displayDir)[0]


def minus():
    global displayDir
    if displayDir != rootDir :
        # Get the next elements in the same folder
        displayDir = next_element(displayDir, 1)

    if displayDir.endswith('.mp3') :
        # Display the artist ID3 tag of the next song.
        tag = TinyTag.get(displayDir)
        return tag.title	#getattr(self,displaytype)
    else :
        #(_, toScreen )= os.path.split(displayDir)
        return os.path.split(displayDir)[0]

def prevElement():
    global displayDir
    #print rootDir
    if displayDir != rootDir :
        displayDir = os.path.dirname(displayDir)
        return os.path.basename(displayDir)
    # print displayDir
    # toScreen = os.path.basename(displayDir)

def nextElement():
    global displayDir
    if os.path.isdir(displayDir) :
    # if folder, enter it
        sortedFileList = sorted(os.listdir(displayDir))
        # Check is not empty folder.
        if sortedFileList != []:
            #remove items beginning with '.'
            sortedFileList = [x for x in sortedFileList if not x.startswith('.') ]
            #print sortedFileList

            firstElement = os.path.join(displayDir,sortedFileList[0])
            if os.path.isdir(firstElement) :
                #print('firstFolder \t%s' %os.path.relpath(firstElement, displayDir))
                return os.path.basename(firstElement)
                #print('toScreen \t%s' %toScreen)
            else :
                (_, file_extension) = os.path.splitext(firstElement)
                if file_extension == '.mp3' :
                    tag = TinyTag.get(firstElement)
                    if tag.title :
                        return tag.title
                    else :
                        return os.path.basename(firstElement)
            displayDir = firstElement

    elif (os.path.isfile(displayDir) ):

        (_, file_extension) = os.path.splitext(displayDir)
        if file_extension == '.mp3' :
            # if .mp3 file, clear next tracks, add it and play it
            CLIENT.clear()

            # Add songs after it in the playlist
            (_, _, filenames) = os.walk(os.path.dirname(displayDir)).next()
            filenames.sort()

            # get the File name :
            (absDirName, fileName) = os.path.split(displayDir)

            # Find its position in the folder array
            indexFile = filenames.index(fileName)

            # Add the next songs in the playlist (+1 because current file already added)
            for index in range(0, len(filenames)) :
                #print('index  \t%s' %index)
                file2add = os.path.join(os.path.relpath(absDirName, rootDir), filenames[index])

                # Remove './' if files begins with it.
                if file2add[0:2] == "./" :
                    tempString = ''
                    tempString = file2add[2:]
                    file2add = tempString
                #print('file2add  \t%s' %file2add)
                CLIENT.add(file2add)

            CLIENT.play(indexFile)
            return client.currentsong()['title']


def repeat(repeat, toggle=False):
  if toggle:
    current = int(CLIENT.status()['repeat'])
    repeat = (not current) # Love this
  CLIENT.repeat(int(repeat))
  return repeat

def random(random, toggle=False):
  if toggle:
    current = int(CLIENT.status()['random'])
    random = (not current) # Love this
  CLIENT.random(int(random))
  return random

def seek(delta):
  try:
    seekDest = int(float(CLIENT.status()['elapsed']) + delta)
    playListID = int(CLIENT.status()['song'])
    CLIENT.seek(playListID, seekDest)
  except Exception, e:
    logging.warning("Issue seeking - elapsed key missing")

def getTrackInfo():
  global T_STATUS
  currentTID = getTrackID()
  for song in PLAYLIST:
    trackID = song["id"]
    if trackID == currentTID:
      T_STATUS = song

def getInfo(lastID=-1):
  global CLIENT
  if CLIENT == None:
    init()
  state = None
  while not state:
    try:
      state = CLIENT.status()
    except Exception, e:
      logging.warning("MPD lost connection while reading status")
      time.sleep(.5)
      CLIENT == None

  if (state['state'] != "stop"):
    if ("songid" in state):
      songID = state['songid']
      if (songID != lastID):
        getTrackInfo()
    if (T_STATUS == None):
      getTrackInfo()
  status = {"status": state, "track": T_STATUS}
  logging.debug("Player Status Requested. Returning:")
  logging.debug(status)
  return status
