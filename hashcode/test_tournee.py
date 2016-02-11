# -*- coding: utf-8 -*-

#Arnaud

from tournee import *
import unittest

class client:
    def __init__(self, r, c):
        self.r = r
        self.c = c

class tournee_testCase(unittest.TestCase):
    def test_nearest_neighbor(self):
        client_list =  [client(0, 10), client(0, 5)]
        self.assertEqual(1, nearest_neighbor(0, 0, client_list))

if __name__ == "__main__":
    unittest.main()
