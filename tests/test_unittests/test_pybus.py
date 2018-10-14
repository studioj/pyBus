"""
# ==============================================================================
# Name:         test_pybus
#
# Purpose:      
#
# Author:       JEFNE
# Created:      14/10/2018
# Copyright:    (c) Jef Neefs 2018
# Licence:      GPLv3
# ==============================================================================
# Extra used pypi modules which may need to be installed:
# pip install nose
# ==============================================================================
"""
from unittest import TestCase


class TestPyBusCommunication(TestCase):
    def test_pybus2_can_be_imported_without_problems(self):
        import pybus2


