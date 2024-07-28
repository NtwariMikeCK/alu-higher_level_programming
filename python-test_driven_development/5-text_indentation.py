#!/usr/bin/python3
"""Unittest for text_indentation function"""
import unittest
from io import StringIO
import sys
text_indentation = __import__('5-text_indentation').text_indentation

class TestTextIndentation(unittest.TestCase):
    def test_simple(self):
        """Test simple string"""
        text = "Hello. How are you? I am fine:"
        expected_output = "Hello.\n\nHow are you?\n\nI am fine:\n\n"
        self.check_output(text, expected_output)
        
    def test_with_spaces(self):
        """Test string with spaces after punctuation"""
        text = "Hello.   How are you?    I am fine:   "
        expected_output = "Hello.\n\nHow are you?\n\nI am fine:\n\n"
        self.check_output(text, expected_output)

    def test_no_punctuation(self):
        """Test string with no punctuation"""
        text = "Hello How are you I am fine"
        expected_output = "Hello How are you I am fine"
        self.check_output(text, expected_output)

    def test_only_punctuation(self):
        """Test string with only punctuation"""
        text = ".?:"
        expected_output = ".\n\n?\n\n:\n\n"
        self.check_output(text, expected_output)

    def test_empty_string(self):
        """Test empty string"""
        text = ""
        expected_output = ""
        self.check_output(text, expected_output)

    def test_type_error(self):
        """Test non-string input"""
        with self.assertRaises(TypeError):
            text_indentation(1234)
    
    def check_output(self, text, expected_output):
        """Helper method to check the output of the function"""
        output = StringIO()
        sys.stdout = output
        text_indentation(text)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
