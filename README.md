[![Build Status](https://travis-ci.com/studioj/pyBus.svg?branch=master)](https://travis-ci.com/studioj/pyBus)
[![Coverage Status](https://coveralls.io/repos/github/studioj/pyBus/badge.svg?branch=master)](https://coveralls.io/github/studioj/pyBus?branch=master)
[![BCH compliance](https://bettercodehub.com/edge/badge/studioj/pyBus?branch=master)](https://bettercodehub.com/)
[![CodeFactor](https://www.codefactor.io/repository/github/studioj/pybus/badge)](https://www.codefactor.io/repository/github/studioj/pybus)

pyBus
=====

**This is a fork of [PyBus](https://github.com/3isenHeiM/pyBus)** by https://github.com/3isenHeiM

**Which is a fork of [PyBus](https://github.com/ezeakeal/pyBus)** by https://github.com/ezeakeal

Main change: control of the RPi **via the buttons on the Radio**.

iBus interface for my E46 BMW written in Python.
This is intended to run on a Raspberry Pi, installed in the E46.
To make interaction with the CAN bus, it's to be used with the USB interface which can be acquired from [Reslers.de](http://www.reslers.de/IBUS/)

my (planned) changes in this fork:
- [ ] TDD greenfielding current functionality
- [ ] deployment via package
- [x] travis integration
- [ ] pypi deployment
- [x] coveralls integration
- [x] bettercodehub integration
- [x] codefactor integration
- [ ] extra bells and whistles


## Overview
There are 2 main components:  
**pyBus.py** - interfaces with the iBus to emulate a CD-Changer  
**pyBus_audio.py** - MPD client that will interpret buttons pressed, and control the music.

Functions foreseen :
* Play/Pause
* Next/Previous
* Nagivate in the folders to play an entire folder.
* View RPM, current speed...

## Tasks
- [x] Configure bluetooth for auto-pairing with any device
- [x] Develop the mpd client to control the audio
- [ ] (in progress) Integrate it into the pyBus
- [ ] Test the integration with the actual CAN bus
- [ ] Have fun

## Controls

These are the foreseen buttons to control the multimedia :

Button | Action
--- | ---
`<` | Parent folder
`>` | Enter folder / Play file
`+` | Next item (file/folder)
`-` | Previous item (file or folder)
`1` | Play/pause
`2` | TBD
`3` | Previous song
`4` | Next song
`5` | Toggle Bluetooth audio
`6` | Display car info (speed, ...)


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
* python, pip-python, python-dev, build-essentials, mpd, python-setuptools
	* `apt-get install python python-setuptools python-pip python-dev build-essenial mpd`
* **Python modules:** python-mpd2, pyserial, tinytag
	* `pip install python-mpd2 pyserial tinytag`

## How to use
* Install the prerequisites above
* Ensure music is available at /Music and that `mpd` is configured to read from there.
* Plug in iBus USB device
* Run: `./pyBus.py -d <PATH to USB Device>`
	* E.g. `./pyBus.py -d /dev/ttyUSB0`

#### Optional arguments:
*  `-h`, `--help` : show this help message and exit
*  `-v`, `--verbose` : Increases verbosity of logging (up to `-vvvv` : info logging).
*  `-d DEVICE`, `--device DEVICE` :   Path to iBus USB interface (Bought from reslers.de)
*  `-o OUTPUT_FILE`, `--output_file OUTPUT_FILE` : Path/Name of log file (log level of 0). If no file specified, output only to std.out
