#!/usr/bin/python

# The MPD module has practically no documentation as far as I know.. so a lot of this is guess-work, albeit educated guess-work
import pprint, os, sys, time, signal, logging
from mpd import (MPDClient, CommandError)
from socket import error as SocketError
import pyBus_core as core

from tinytag import TinyTag		# To read ID3 tags

#####################################
# GLOBALS
#####################################
HOST     = 'localhost'
PORT     = '6600'
PASSWORD = False
CON_ID   = {'host':HOST, 'port':PORT}
VOLUME   = 90

CLIENT   = None
ROOT_DIR = '/home/kruger/Music'
CURRENT_DIR = ROOT_DIR
DISPLAY_DIR = 'Hello'
TO_SCREEN = "Welcome"

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
  global CLIENT, ROOT_DIR, CURRENT_DIR, DISPLAY_DIR, TO_SCREEN
  ## MPD object instance
  CLIENT = MPDClient()
  if mpdConnect(CLIENT, CON_ID):
    logging.info('Connected to MPD server')

  else:
    logging.critical('Failed to connect to MPD server')
    logging.critical("Sleeping 1 second and retrying")
    time.sleep(1)
    init()

# Updates MPD library
def update():
  logging.info('Updating MPD Library')
  CLIENT.update()

def addAll():
  CLIENT.clear() # Clear current playlist
  CLIENT.add('/') # Add all songs in library (TEMP)
    
def quit():
  if CLIENT:
    CLIENT.disconnect()

def play():
  CLIENT.play()

def stop():
  if CLIENT:
    CLIENT.stop()

def pause():
  CLIENT.pause()

def next():
  CLIENT.next()

def previous():
  CLIENT.previous()

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
  
########### FUNCTIONS ADDED
def getCurrentTrack():
	global CLIENT
	return CLIENT.currentsong()['title']



def togglePlayPause():
  global CLIENT
  status = CLIENT.status()
  if (status['state']=='play'):
    client.pause()
    toScreen = "Pause"
  elif (status['state']=='stop' or status['state']=='pause'):
    client.play()
    toScreen = client.currentsong()['title']

###########




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

def getInfoByPath(filePath):
  for song in PLAYLIST:
   path = song["file"]
   if path == filePath:
     return song

def addSong(filepath):
  global PLAYLIST
  if (getInfoByPath(filepath) == None):
    CLIENT.add(filepath)
    PLAYLIST = CLIENT.playlistinfo()

def removeSong(filepath):
  global PLAYLIST
  song = getInfoByPath(filepath)
  CLIENT.deleteid(song['id'])
  PLAYLIST = CLIENT.playlistinfo()

def playSong(filepath):
  song = getInfoByPath(filepath)
  CLIENT.playid(song['id'])

def  getTrackID():
  if ("songid" not in CLIENT.status()):
    logging.warning("MPD status does not contain songID. Please investigate following status:")
    logging.warning(CLIENT.status())
  try:
    currentTID = CLIENT.status()['songid']
    return currentTID
  except e:
    logging.warning("Unexpected Exception occured:")
    logging.warning(traceback.format_exc())
    return 0
