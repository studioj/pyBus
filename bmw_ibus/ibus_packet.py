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
        self.length = bytearray.fromhex(str(len(self.destination + self.message) + 1).zfill(2))
        self.xor = self.__calculate_xor(self.source + self.length + self.destination + self.message)
        return self.source + self.length + self.destination + self.message + self.xor

    def __calculate_xor(self, packet_to_xor):
        chk = 0
        packet_to_xor.append(0)
        for p in packet_to_xor:
            chk ^= p
        return chk.to_bytes(1, "big")
