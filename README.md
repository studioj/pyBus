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

