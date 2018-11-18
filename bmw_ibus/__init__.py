"""
# ==============================================================================
# Name:         __init__.py
#
# Purpose:      
#
# Author:           Jef Neefs
# Created:          13/08/2018
# Copyright:        (c) Jef Neefs 2018
# Licence:          GPLv3
# ==============================================================================
# Extra used pypi modules which may need to be installed:
# pip install nose
# ==============================================================================
"""

from serial.tools.list_ports import comports as list_comports
from serial import Serial

RESLERS_DEVICE_DESCRIPTION = "CP2102 USB to UART Bridge Controller"


class IBus(object):
    def __init__(self):
        self.__serial = None

    def connect(self):
        list_of_comports = list_comports()
        for serial_device in list_of_comports:
            if serial_device.description == RESLERS_DEVICE_DESCRIPTION:
                self.__serial = Serial(serial_device.device)
