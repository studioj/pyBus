"""
# ==============================================================================
# Name:         test_bmw-ibus
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
from unittest import TestCase

import serial
from mock import patch

from bmw_ibus import IBus


class Dummyclass(object):
    def __init__(self, device, description):
        self.device = device
        self.description = description


class TestBMWiBusSerialConnection(TestCase):
    def test_all_serial_ports_are_requested_from_the_system_at_connect(self):
        with patch("bmw_ibus.list_comports") as comports_mock:
            with patch("bmw_ibus.Serial") as mocked_serial:
                comports_mock.return_value = [Dummyclass('/dev/ttyAMA0', 'ttyAMA0'),
                                              Dummyclass('/dev/ttyUSB0', 'CP2102 USB to UART Bridge Controller')]
                ibus = IBus()
                ibus.connect()
                comports_mock.assert_called_once()

    def test_that_the_connect_statement_connects_to_the_resler_serial_port_if_it_is_connected(self):
        with patch("bmw_ibus.list_comports") as comports_mock:
            comports_mock.return_value = [Dummyclass('/dev/ttyUSB0', 'CP2102 USB to UART Bridge Controller'),
                                          Dummyclass('/dev/ttyAMA0', 'ttyAMA0')]
            with patch("bmw_ibus.Serial") as mocked_serial:
                ibus = IBus()
                ibus.connect()
                mocked_serial.assert_called_once_with(comports_mock.return_value[0].device, parity=serial.PARITY_EVEN)

    def test_that_serial_connects_to_the_resler_serial_port_if_it_is_connected_even_if_it_is_not_the_first(self):
        with patch("bmw_ibus.list_comports") as comports_mock:
            comports_mock.return_value = [Dummyclass('/dev/ttyAMA0', 'ttyAMA0'),
                                          Dummyclass('/dev/ttyAMA1', 'ttyAMA1'),
                                          Dummyclass('/dev/ttyUSB0', 'CP2102 USB to UART Bridge Controller')]
            with patch("bmw_ibus.Serial") as mocked_serial:
                ibus = IBus()
                ibus.connect()
                mocked_serial.assert_called_once_with(comports_mock.return_value[2].device, parity=serial.PARITY_EVEN)
