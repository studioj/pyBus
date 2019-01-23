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
import re
# noinspection PyPackageRequirements
from serial.tools.list_ports import comports as list_comports
# noinspection PyPackageRequirements
from serial import Serial, EIGHTBITS, PARITY_EVEN, STOPBITS_ONE

RESLERS_DEVICE_DESCRIPTION = "CP210. USB .*UART"
RESLERS_DEVICE_PARITY = PARITY_EVEN


class IBus(object):
    def __init__(self):
        self.__serial_connection = None

    def connect(self):
        list_of_comports = list_comports()
        for serial_device in list_of_comports:
            if re.match(RESLERS_DEVICE_DESCRIPTION, serial_device.description):
                self.__serial_connection = Serial(serial_device.device, parity=RESLERS_DEVICE_PARITY)
