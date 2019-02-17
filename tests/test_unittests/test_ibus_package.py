"""
# ==============================================================================
# Name:             test_ibus_package
#                   -
# Purpose:          -
#                   -
#                   -
# Author:           Jef Neefs
# Created:          12/02/2019
# Copyright:        (c) Jef Neefs 2019
# Licence:          GPLv3
# ==============================================================================
# Extra used pypi modules which may need to be installed:
#
# ==============================================================================
"""
import unittest

from mock import MagicMock

from bmw_ibus.ibus_packet import IBusPacket


class TestIBusPacket(unittest.TestCase):
    def test_ibus_packet_contains_a_source_destination_and_message(self):
        # Given
        source = MagicMock()
        destination = MagicMock()
        message = MagicMock()
        # When
        ibus_packet = IBusPacket(source, destination, message)
        # Then
        self.assertEqual(source, ibus_packet.source)
        self.assertEqual(destination, ibus_packet.destination)
        self.assertEqual(message, ibus_packet.message)

    def test_ibus_packet_has_a_get_raw_functionality_which_returns_a_usable_bytearray_for_serial_driver_seat(self):
        # Given move driver seat forward message of 3F06720C01010047
        source = bytearray.fromhex("3F")
        destination = bytearray.fromhex("72")
        message = bytearray.fromhex("0C010100")
        # When
        ibus_packet = IBusPacket(source, destination, message)
        raw_data = ibus_packet.get_raw()
        # Then
        self.assertIsInstance(raw_data, bytearray)
        self.assertEqual(bytearray.fromhex("3F06720C01010047"), raw_data)

    def test_ibus_packet_has_a_get_raw_functionality_which_returns_a_usable_bytearray_for_serial_vol_up(self):
        # Given move driver seat forward message of 50046832111f
        source = bytearray.fromhex("50")
        destination = bytearray.fromhex("68")
        message = bytearray.fromhex("3211")
        # When
        ibus_packet = IBusPacket(source, destination, message)
        raw_data = ibus_packet.get_raw()
        # Then
        self.assertIsInstance(raw_data, bytearray)
        self.assertEqual(bytearray.fromhex("50046832111f"), raw_data)
