# -*- coding: utf-8 -*-

#Arnaud

#we have to define an array with the clients which will be used only there

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
                if inventory[itemId] > 0 and client.demands[itemId] > 0:
                    av_clients.append(client)
                    break
    return av_clients

def square_distance(r1, c1, r2, c2):
    return ((r1 - r2)**2) + ((c1 - c2)**2)
