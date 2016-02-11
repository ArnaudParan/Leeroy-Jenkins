# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 21:15:49 2016

@author: Simon
"""
WHT_LIMIT = 100     

def weight(package):
    pack_weight = 0
    for key in package:
        pack_weight += products[key].weight
    return pack_weight  

###### CLASSE DRONE ######

class Drone:
    def __init__(self,drone_id,r,c,package_list):
        self.id = drone.id
        self.r = r
        self.c = c
        self.package = to_dict(package_list)
        self.cost = 0
        self.wht = weight(self.package)
        self.wht_limit = WHT_LIMIT
        
    def move(self, to_r, to_c):
        self.cost += int(square_distance(self.r, self.c, to_r, to_c)) + 1
        self.r = to_r
        self.c = to_c
        
    def carriable(self, order):
        is_deliverable = True
        after_delivery = add_dict(package, order)
        for key in after_delivery:
            if after_delivery[key] < 0 and self.wht + weight(order) <= self.wht_limit:
                is_deliverable = False
        return is_deliverable
        
    def take(self, order):
        if(self.deliverable(order)):
            add_dict(self.package, order)
            self.wht += weight(order)
            
class Product:
    def __init__(self, prod_id, wht):
        self.id = prod_id
        self.wht = wht

            
        
        