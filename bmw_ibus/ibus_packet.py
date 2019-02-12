"""
# ==============================================================================
# Name:             ibus_packet
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


class IBusPacket(object):
    def __init__(self, source, destination, message):
        self.source = source
        self.destination = destination
        self.message = message

    def get_raw(self):
        return bytearray.fromhex("3F06720C01010047")
