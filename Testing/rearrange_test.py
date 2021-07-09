#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Nguyen, Iris"
        expected = "Iris Nguyen"
        self.assertEqual(rearrange_name(testcase), expected)
    #Corner cases:
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Dante"
        expected = "Dante"
        self.assertEqual(rearrange_name(testcase), expected)
unittest.main()
