# test_stratabeam.py
"""
Tests for StrataBeam module.
"""

import unittest
from stratabeam import StrataBeam

class TestStrataBeam(unittest.TestCase):
    """Test cases for StrataBeam class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StrataBeam()
        self.assertIsInstance(instance, StrataBeam)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StrataBeam()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
