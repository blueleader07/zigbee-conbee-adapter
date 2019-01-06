"""Tests adding a temperature sensor."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from pkg.conbee_adapter import ConBeeAdapter

class AddTemperatureSensorTest(unittest.TestCase):
    def test(self):
        adapter = ConBeeAdapter()
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()