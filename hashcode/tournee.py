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

def square_distance(r1, c1, r2, c2):
    return ((r1 - r2)**2) + ((c1 - c2)**2)
