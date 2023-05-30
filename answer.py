import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class GameData:
    ncells : int
    mdata : list
    nbases : int
    my_base : int
    en_base : int
    neighs : list
    egg : int
    nlines : int
    turn : int
    near : bool
    action : str
    ngold : int

gdata = GameData()

gdata.ngold = 0
gdata.ncells = int(input())  # amount of hexagonal cells in this map
gdata.mdata = [[0] * 9] * gdata.ncells
for i in range(gdata.ncells):
    # _type: 0 for empty, 1 for eggs, 2 for crystal
    # initial_resources: the initial amount of eggs/crystals on this cell
    # neigh_0: the index of the neighbouring cell for each direction
    _type, initial_resources, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
    if _type == 2:
        gdata.ngold += 1
    gdata.mdata[i] = [_type, initial_resources, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5, 0]
gdata.nbases = int(input())
for i in input().split():
    gdata.my_base = int(i)
for i in input().split():
    gdata.en_base = int(i)

gdata.neighs = []
for i in range(6):
    gdata.neighs.append(gdata.mdata[gdata.my_base][i + 2])

gdata.egg = -1
gdata.nlines = 0
gdata.turn = 0

def grab_neigh():
    for neigh in gdata.neighs:
        if neigh >= 0 and gdata.nlines < 3:
            if gdata.mdata[neigh][0] == 1:
                gdata.nlines += 1
                gdata.action += "LINE " + str(gdata.my_base) + " " + str(neigh) + " 1; MESSAGE lol;"
                gdata.near = True

# game loop
while True:
    gdata.turn += 1
    gdata.nlines = 0
    gdata.action = ""
    gdata.near = False

    for i in range(gdata.ncells):
        # resources: the current amount of eggs/crystals on this cell
        # my_ants: the amount of your ants on this cell
        # opp_ants: the amount of opponent ants on this cell
        resources, my_ants, opp_ants = [int(j) for j in input().split()]
        gdata.mdata[i][8] = resources
        if resources == 0:
            gdata.mdata[i][0] = 0

    # Search cells directly adjacent to base first
    grab_neigh()
    
    # Then search for a big egg cell and store its location
    for idx, cell in enumerate(gdata.mdata):
        if cell[0] == 1 and cell[8] >= 20 and gdata.egg == -1 and not gdata.near:
            gdata.egg = idx
            
    # Then start gathering the eggs
    if gdata.egg >= 0 and gdata.egg != -1 and not gdata.near and gdata.ngold > 3:
        gdata.nlines += 1
        gdata.action += "LINE " + str(gdata.my_base) + " " + str(gdata.egg) + " 1; MESSAGE " + str(gdata.ngold) + ";"
    
    # Then grab all the crystals
    for idx, cell in enumerate(gdata.mdata):
        if cell[0] == 2 and gdata.nlines < 9 and not gdata.near:
            gdata.nlines += 1
            gdata.action += "LINE " + str(gdata.my_base) + " " + str(idx) + " " + str(int(cell[8] / 2) + 100) + ";"
    
    print(gdata.action) 

