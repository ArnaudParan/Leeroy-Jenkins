# -*- coding: utf-8 -*-

#Arnaud

from tournee import *
import unittest

class client:
    def __init__(self, r, c, inventory):
        self.r = r
        self.c = c
        self.demands = inventory

class drone:
    def __init__(self, r, c, package):
        self.r = r
        self.c = c
        self.package = package

class tournee_testCase(unittest.TestCase):
    def test_nearest_neighbor(self):
        client_list =  [client(0, 10, []), client(0, 5, [])]
        self.assertEqual(1, nearest_neighbor(0, 0, client_list))

    def test_available_clients(self):
        client_inv1 = {0: -1, 1: -2 , 2: -4}
        client_inv2 = {0: -3, 1: -2 , 3: -1}
        client1 = client(0, 0, client_inv1)
        client2 = client(0, 0, client_inv2)
        client_list = [client1, client2]
        inventory = {3: 4}
        current = available_clients(inventory, client_list)
        self.assertEqual([client2], current)

    def test_item_to_deliver(self):
        client_inv1 = {0: -1, 1: -2 , 2: -1}
        client1 = client(0, 0, client_inv1)
        inventory = {2: 4}
        current = item_to_deliver(inventory, client1)
        self.assertEqual((2, 1), current)

    def test_incr_drone_time(self):
        client1 = client(0, 10, {})
        client2 = client(1, 2, {})
        client_list =  [client1, client2]
        t_arr = [1, 2]
        curr_drone = drone(0, 0, {})
        incr_drone_time(curr_drone, client2, t_arr, 1)
        self.assertEqual([1, 6], t_arr)

if __name__ == "__main__":
    unittest.main()
