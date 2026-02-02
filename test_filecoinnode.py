# test_filecoinnode.py
"""
Tests for FilecoinNode module.
"""

import unittest
from filecoinnode import FilecoinNode

class TestFilecoinNode(unittest.TestCase):
    """Test cases for FilecoinNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FilecoinNode()
        self.assertIsInstance(instance, FilecoinNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FilecoinNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
