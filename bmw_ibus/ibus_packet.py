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
        self.length = 0
        self.xor = 0

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

    def __str__(self):
        return f"Source: {devices[str(self.source)]}, Destination: {devices[str(self.destination)]}, Message: .*"


# retrieved partially from http://web.comhem.se/bengt-olof.swing/ibusdevicesandoperations.htm
devices = {str(bytearray.fromhex("00")): "Broadcast,GM",
           str(bytearray.fromhex("08")): "SHD",
           str(bytearray.fromhex("18")): "CD Player",
           str(bytearray.fromhex("24")): "HKM",
           str(bytearray.fromhex("28")): "FUM",
           str(bytearray.fromhex("30")): "CCM",
           str(bytearray.fromhex("3B")): "NAV, GT",
           str(bytearray.fromhex("3F")): "DIA",
           str(bytearray.fromhex("40")): "FBZV",
           str(bytearray.fromhex("43")): "Menu Screen, GTF",
           str(bytearray.fromhex("44")): "EWS",
           str(bytearray.fromhex("46")): "CID",
           str(bytearray.fromhex("47")): "FMBT",
           str(bytearray.fromhex("50")): "MFL, Multi Functional Steering Wheel Buttons",
           str(bytearray.fromhex("51")): "MML",
           str(bytearray.fromhex("5B")): "IHK",
           str(bytearray.fromhex("60")): "PDC",
           str(bytearray.fromhex("66")): "CDCD",
           str(bytearray.fromhex("68")): "RAD, Radio",
           str(bytearray.fromhex("6A")): "DSP",
           str(bytearray.fromhex("70")): "RDC",
           str(bytearray.fromhex("72")): "SM",
           str(bytearray.fromhex("73")): "SDRS",
           str(bytearray.fromhex("76")): "CDCD",
           str(bytearray.fromhex("7F")): "NAVE",
           str(bytearray.fromhex("80")): "IKE",
           str(bytearray.fromhex("9B")): "MMR",
           str(bytearray.fromhex("9C")): "CVM",
           str(bytearray.fromhex("A0")): "FMID",
           str(bytearray.fromhex("A4")): "ACM",
           str(bytearray.fromhex("A7")): "FHK",
           str(bytearray.fromhex("A8")): "NAVC",
           str(bytearray.fromhex("AC")): "EHC",
           str(bytearray.fromhex("B0")): "SES",
           str(bytearray.fromhex("BB")): "TV, NAVJ",
           str(bytearray.fromhex("BF")): "LCM, Light Control Module. GLO",
           str(bytearray.fromhex("C0")): "MID, Multi Information Display",
           str(bytearray.fromhex("C8")): "Telephone",
           str(bytearray.fromhex("D0")): "Navigation Location, LKM",
           str(bytearray.fromhex("D7")): "USED BY ME: PC",
           str(bytearray.fromhex("D8")): "USED BY ME: GPS and Powercontrol Module",
           str(bytearray.fromhex("DA")): "SMAD",
           str(bytearray.fromhex("E0")): "IRIS",
           str(bytearray.fromhex("E7")): "OBC Textbar, ANZV",
           str(bytearray.fromhex("E8")): "ISP",
           str(bytearray.fromhex("ED")): "Lights, wipers, seat memory, TV",
           str(bytearray.fromhex("F0")): "Bordmonitor Buttons",
           str(bytearray.fromhex("F5")): "CSU",
           str(bytearray.fromhex("FF")): "Broadcast, LOC",
           }
