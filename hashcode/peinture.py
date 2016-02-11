# -*- coding: utf-8 -*-

"""
Fonctions.py
"""


import csv, os, sys

import numpy as np
import random

# convertie en np 0 1
def format_numpy(nr, nc, data):
    res = np.zeros([nr,nc])
    for i in range(0,nr):
        for j in range(0,nc):
            if data[i][j] == '#':
                res[i][j] = 1
    return res


def write_commands(output, output_path, file_number=1):
    save_folder = os.path.dirname(output_path)
    save_file = os.path.basename(output_path)

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    #print "Writting results in file : " + output_path + " ..." 

    # SAVE HERE
    with open(save_folder+'/'+str(file_number)+save_file,'wb') as sf:
        #sf.write( [ ';'.join(l)+'\n' for l in data ] )
        sf.write(str(len(output))+'\n')

        for line in output:
            sf.write(line+'\n')


def commands(to_draw, to_erase):
    coms = []
    # drawing commands
    for d in to_draw:
        if d[0] == "LINE":
            line = d[1]
            coms.append('PAINT_LINE '
                        + str(line[0][0]) + ' '
                        + str(line[0][1]) + ' '
                        + str(line[1][0]) + ' '
                        + str(line[1][1]) )
        else:
            carre = d[1]
            coms.append('PAINT_SQUARE '
                        + str(carre[0]+carre[2]/2) + ' '
                        + str(carre[1]+carre[2]/2) + ' '
                        + str(carre[2]/2) )
    # erasing comands
    for e in to_erase:
        coms.append('ERASE_CELL ' + str(e[0]) + ' ' + str(e[1]))

    return coms


def chercher_liste_points(nr,nc,data):
    liste_points = set()
    for i in range(0,nr):
        for j in range(0,nc):
            if data[i][j]==1:
                liste_points.add((i,j))
    return liste_points

def calcule_score(uns, zeros):
    return ( 1.0*uns/(zeros+1) )**2

def grandit_ligneh(indices, nr, nc, data):
    elemh = set()
    elemh.add(indices)
    ligneh = list(indices)
    eraseh = set()
    r,c = indices
    elems = [(elemh,eraseh,ligneh)] # keep memory of all tries
    # grow right
    while True:
        c+=1
        if c >= nc:
            break
        if data[r,c] == 1:
            elemh.add((r,c))
        elif data[r,c] == 2:
            ligneh[1] = c-1
            elems.append((elemh,eraseh,ligneh))
            continue
        elif c+1 < nc and data[r,c+1] == 1:
            eraseh.add((r,c))
            elemh.add((r,c+1))
            c+=1
        elif c+1 < nc and data[r,c+1] == 2:
            eraseh.add((r,c))
            ligneh[1] = c-1
            elems.append((elemh,eraseh,ligneh))
            c+=1
        else :
            break

    ligneh[1] = c-1
    c = indices[1]

    # grow left
    while True:
        c-=1
        if c < 0:
            break
        if data[r,c] == 1:
            elemh.add((r,c))
        elif data[r,c] == 2:
            ligneh[0] = c+1
            elems.append((elemh,eraseh,ligneh))
        elif c-1 > 0 and data[r,c-1] == 1:
            eraseh.add((r,c))
            elemh.add((r,c-1))
            c-=1
        elif c-1 > 0 and data[r,c-1] == 2:
            eraseh.add((r,c))
            ligneh[0] = c+1
            elems.append((elemh,eraseh,ligneh))
            c-=1
        else :
            break

    ligneh[0] = c+1

    # look for best elemh and eraseh
    scores = [ len(elemh) - len(eraseh) for elemh,eraseh,l in elems ]
    best = np.argmax(scores)

    elemh, erash, ligneh = elems[best]

    return ( (r,ligneh[0]),(r,ligneh[1]) ), elemh, eraseh


def grandit_lignev(indices, nr, nc, data):
    elemv = set()
    elemv.add(indices)
    lignev = list(indices)
    erasev = set()
    r,c = indices
    elems = [(elemv,erasev,lignev)] # keep memory of all tries
    # grow down
    while True:
        r+=1
        if r >= nr:
            break
        if data[r,c] == 1:
            elemv.add((r,c))
        elif data[r,c] == 2:
            lignev[0] = r-1
            elems.append((elemv,erasev,lignev))
        elif r+1 < nr and data[r+1,c] == 1:
            erasev.add((r,c))
            elemv.add((r+1,c))
            r+=1
        elif r+1 < nr and data[r+1,c] == 2:
            erasev.add((r,c))
            lignev[0] = r-1
            elems.append((elemv,erasev,lignev))
            r+=1
        else :
            break

    lignev[0] = r-1
    r = indices[0]

    # grow up
    while True:
        r-=1
        if r < 0:
            break
        if data[r,c] == 1:
            elemv.add((r,c))
        elif data[r,c] == 2:
            lignev[1] = r+1
            elems.append((elemv,erasev,lignev))   
        elif r-1 > 0 and data[r-1,c] == 1:
            erasev.add((r,c))
            elemv.add((r-1,c))
            r-=1
        elif r-1 > 0 and data[r-1,c] == 1:
            erasev.add((r,c))
            r-=1
        elif r+1 < nr and data[r-1,c] == 2:
            erasev.add((r,c))
            lignev[1] = r+1
            elems.append((elemv,erasev,lignev))
            r-=1
        else :
            break

    lignev[1] = r+1

    # look for best elemv and erasev
    scores = [ len(elemv) - len(erasev) for elemv,erasev,l in elems ]
    best = np.argmax(scores)

    elemv, erash, lignev = elems[best]

    return ( (lignev[1],c),(lignev[0],c) ) , elemv, erasev


def compte_carre(d,nr,nc,data):
    carre = data[ d[0]:d[0]+d[2] , d[1]:d[1]+d[2] ]
    # regarde si le carre est valides
    zeros = np.sum( carre == 0 )
    uns = np.sum( carre == 1 )
 
    return uns, zeros
   

def cherche_indices_carre(carre,data):
    indices_1 = set()
    indices_0 = set()
    for i in range(carre[0],carre[0]+carre[2]):
        for j in range(carre[1],carre[1]+carre[2]):
            if data[i,j]==1:
                indices_1.add( (i,j) )
            if data[i,j]==0:
                indices_0.add( (i,j) )

    return indices_1, indices_0


def grandit_carre(indices, nr, nc, data, NTRIES = 4):
    # le carre sera definit par son coin top-left et sa taille impaire
    carre = list(indices) + [1]
    score_carre = 1
    meilleur = carre
    tries=0 # tentatives de grosir

    #elems = [(elemc,erasec,carre,score_carre)]

    # 2 boucles: une sur les dispositions, l'autres sur les dimensions
    
    while True: # boucle sur les dimensions

        # 8 dispositions à tester : on prendra la meilleure
        dispositions = []
        r,c,s = carre

        if c-0>=0 and c+s-1+2 < nc:
            if r-0>=0 and r+s-1+2 < nr :
                dispositions.append([r-0,c-0,s+2])

            if r-1>=0 and r+s-1+1 < nr :
                dispositions.append([r-1,c-0,s+2])

            if r-2>=0 and r+s-1+ 0 < nr :
                dispositions.append([r-2,c-0,s+2])


        if c-1>=0 and c+s-1+1 < nc:
            if r-0>=0 and r+s-1+2 < nr :
                dispositions.append([r-0,c-1,s+2])

            if r-1>=0 and r+s-1+1 < nr :
                dispositions.append([r-1,c-1,s+2])

            if r-2>=0 and r +s-1+ 0 < nr :
                dispositions.append([r-2,c-1,s+2])


        if c-2>=0 and c+s-1+0 < nc:
            if r-0>=0 and r+s-1+2 < nr :
                dispositions.append([r-0,c-2,s+2])

            if r-1>=0 and r+s-1+1 < nr :
                dispositions.append([r-1,c-2,s+2])

            if r-2>=0 and r +s-1+ 0 < nr :
                dispositions.append([r-2,c-2,s+2])
        

        if not dispositions: # cannot be better
            break

        somme_totale = (s+2)*(s+2)
        scores = []
        for d in dispositions:
            uns, zeros = compte_carre(d,nr,nc,data)
            #scores.append( uns - zeros ) # score nul si carre non valide = OK
            scores.append( calcule_score(uns,zeros) ) # score nul si carre non valide = OK
        
        best_index = np.argmax(scores)
        carre = dispositions[best_index]
    
        if scores[best_index] > score_carre : # si carre valide et meilleur
        #if scores[best_index] >= score_carre : # si carre valide et meilleur
            meilleur = carre
            score_carre = scores[best_index]
            tries=0 # remise à 0 des tentatives d'aller plus loin

        else:
            tries+=1
            if tries > NTRIES:
                break # amélioration pour explorer au delà des deux ici

    elemc, erasec = cherche_indices_carre(meilleur,data)

    return meilleur, elemc, erasec


def process_data_method1(nr, nc, data, squares=True, method=1):
    to_draw = set() # set of command (command, args)
    to_erase = set() # set of indices (,)
    # pour chaque pixel noir, on essaie de faire grandir une ligne ou un carré à partir de lui

    # initialisation de la liste des points noirs
    liste_points = chercher_liste_points(nr,nc,data)
    taille_depart = len(liste_points)
    i = len(liste_points)/100

    # init random
    random.seed()

    # on continue tant que la liste des pixels à traiter est non vide
    while liste_points:
        # show len of set
        if method==1:
            if len(liste_points)/100 < i:
                i= len(liste_points)/100
                sys.stdout.write("\rProgress : %i%% \r" % (100*len(liste_points)/taille_depart) )
                sys.stdout.flush()
    
        
        # on en choisit un aleatoirement
        indices = random.sample(liste_points, 1)[0]
        # on va chercher à faire grandir une ligne h ou v ou un carré à partir de ce point
        ligneh, elemh, eraseh = grandit_ligneh(indices, nr, nc, data)
        lignev, elemv, erasev = grandit_lignev(indices, nr, nc, data)
        if squares:
            carre, elemc, erasec = grandit_carre(indices, nr, nc, data, 4)

        # keep best scoring element
        #scoreh = (len(elemh) - len(eraseh))
        scoreh = calcule_score( len(elemh), len(eraseh) )
        #scorev = (len(elemv) - len(erasev))
        scorev = calcule_score( len(elemv), len(erasev) )
        if squares:
            #scorec = (len(elemc) - len(erasec))
            scorec = calcule_score( len(elemc), len(erasec) )


        if squares:
            elems = ( (ligneh,elemh,eraseh), (lignev,elemv,erasev), (carre,elemc,erasec)  )
            scores = [scoreh, scorev, scorec]
        else:
            elems = ( (ligneh,elemh,eraseh), (lignev,elemv,erasev) )
            scores = [scoreh, scorev]

        best = np.argmax(scores)


        if best == 2:
            to_draw.add(("SQUARE", tuple(carre) ))    # add square
        else:
            to_draw.add(("LINE", elems[best][0] ))    # add line

        # paint on best_erase elements
        for ind in elems[best][2]:
            data[ind[0],ind[1]] = 2
        for ind in elems[best][1]:
            data[ind[0],ind[1]] = 2

        # update to_erase elements
        to_erase |= elems[best][2]

        # update liste_points
        liste_points -= elems[best][1]

        #raw_input()

    return commands(to_draw, to_erase)
