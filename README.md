pyBus
=====

**This is a fork of [PyBus](https://github.com/ezeakeal/pyBus)**

Main change : control of the RPi **via the buttons on the Radio**.

iBus interface for my E46 BMW written in Python.
This is intended to run on a Raspberry Pi, installed in the E46.
To make interaction with the CAN bus, it's to be used with the USB interface which can be acquired from [Reslers.de](http://www.reslers.de/IBUS/)


## Overview
There are 2 main components:  
**pyBus.py** - interfaces with the iBus to emulate a CD-Changer  
**pyBus_audio.py** - MPD client that will interpred buttons pressed, and control the music. Function foreseen : 
* Play/Pause
* Next/Previous
* Nagivate in the folders to play an entire folder.
* View RPM, current speed...

## Tasks
- [x] Configure bluetooth for auto-pairing with any device
- [x] Develop the mpd client to control the audio
- [x] Integrate it into the pyBus
- [ ] Test the integration with the actual CAN bus
- [ ] Have fun

## Controls

These are the foreseen buttons to control the multimedia : 

Button | Action | | Button | Action
--- | ---| --- |--- | ---
`>` | Parent folder | | `1` | Play/pause 
`>` | Enter folder / Play file | | `2` | TBD
`+` | Next item (file/folder) | | `3` | Previous song
`-` | Previous item (file or folder) | | `4` | Next song
 | | | |`5`| Toggle Bluetooth audio
 | | | |`6`| Display car info (speed, ...)


### Useful links
http://linux.die.net/man/5/mpd.conf   
http://miro.oorganica.com/raspberry-pi-mpd/   
http://web.comhem.se/bengt-olof.swing/ibusdevicesandoperations.htm   
https://pythonhosted.org/python-mpd2/

### Warning
All software is in early alpha stages!

### Architecture/Operation
Soooon..

## Pre-Requisites
* python, mpd, python-setuptools
	* `apt-get install python python-setuptools mpd`
* **Python modules:** termcolor, web.py, python-mpd, pyserial
	* `easy_install termcolor web.py python-mpd pyserial`
## How to use
* Install the prerequisites above
* Ensure music is available at /Music and that mpd is configured to read from there (best test mpc using mpc prior)
* Plug in iBus USB device
* Run: `./pyBus.py <PATH to USB Device>`
	* E.g. `./pyBus.py /dev/ttyUSB0`

