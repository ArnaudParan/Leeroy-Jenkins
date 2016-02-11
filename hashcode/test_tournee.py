# -*- coding: utf-8 -*-

#Arnaud

from tournee import *
import unittest

class client:
    def __init__(self, r, c, inventory):
        self.r = r
        self.c = c
        self.demands = inventory

class tournee_testCase(unittest.TestCase):
    def test_nearest_neighbor(self):
        client_list =  [client(0, 10, []), client(0, 5, [])]
        self.assertEqual(1, nearest_neighbor(0, 0, client_list))

    def test_available_clients(self):
        client_inv1 = {0: 1, 1: 2 , 2: 4}
        client_inv2 = {0: 3, 1: 2 , 3: 1}
        client1 = client(0, 0, client_inv1)
        client2 = client(0, 0, client_inv2)
        client_list = [client1, client2]
        inventory = {3: 4}
        current = available_clients(inventory, client_list)
        self.assertEqual([client2], current)

if __name__ == "__main__":
    unittest.main()
