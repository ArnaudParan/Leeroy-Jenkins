# -*- coding: utf-8 -*-

import math

#Arnaud

#we have to define an array with the clients which will be used only there

#warning, the client_list is custom
def tournees(drones, client_list, initial_time):
    dronesTimes = initial_time
    #select the min time drone
    #take his nearest neighbor ##
    #take the item to deliver, and the number ##
    #deliver the item ##
    #add time

def nearest_neighbor(initR, initC, client_list):
    currClientId = 0
    client = client_list[currClientId]
    currMinDist = square_distance(client.r, client.c, initR, initC)
    for clientId in range(len(client_list)):
        client = client_list[clientId]
        dist = square_distance(client.r, client.c, initR, initC)
        if dist < currMinDist:
            currClientId = clientId
            currMinDist = dist
    return currClientId

def available_clients(inventory, client_list):
    av_clients = []
    for client in client_list:
        for itemId in client.demands:
            if itemId in inventory:
                if inventory[itemId] > 0 and client.demands[itemId] < 0:
                    av_clients.append(client)
                    break
    return av_clients

def item_to_deliver(inventory, client):
    for itemId in client.demands:
        if itemId in inventory:
            nbInv = inventory[itemId]
            nbDem = client.demands[itemId]
            if nbInv > 0 and nbDem < 0:
                return itemId, min(nbInv, -nbDem)

def deliver_item(drone, client, itemId, nbItem):
    client.demands[clientId] = client.demands[clientId]  + nbItem
    drone.package[clientId] = drone.package[clientId]  - nbItem

def movement_time(r1, c1, r2, c2):
    sq_dist = square_distance(r1, c1, r2, c2)
    dist = math.sqrt(sq_dist)
    return math.ceil(dist)

def incr_drone_time(drone, client, times_array, droneId):
    mov_time = movement_time(drone.r, drone.c, client.r, client.c) + 1
    times_array[droneId] = times_array[droneId] + mov_time

def square_distance(r1, c1, r2, c2):
    return ((r1 - r2)**2) + ((c1 - c2)**2)

