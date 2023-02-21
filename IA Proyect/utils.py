import constants
import os, sys

def is_int(mystring):
    try:
        temp = int(mystring)
        return True
    except:
        return False

def key_value(mystring, mydict):
    myint = mystring.find(":")
    if myint == -1:
        s = "Error! : was not found in mystring: {}".format(mystring)
        raise ValueError(s)
    tag = mystring[0:myint].strip()
    value = mystring[myint+1:].strip()
    if len(tag) == 0:
        raise ValueError("Error")
    if len(value) == 0:
        raise ValueError("Error")
    mydict[tag] = int(value) if is_int(value) else value
    return mydict

def jugadorposicionmap():
    x, y = -1, -1
    filepath = os.path.join("data", constants.MAPA)
    with open(filepath, "r") as f:
        mytiles = f.readlines()
        mytiles = [i.strip() for i in mytiles if len(i.strip()) > 0]
    for col, tiles in enumerate(mytiles):
        for row, tile in enumerate(tiles):
            if tile == 'p':
                x = row
                y = col
    return x, y

def read_data_file(filepath, num_of_fields):
    big_list = []
    with open(filepath, "r") as f:
        mylines = f.readlines()
        mylines = [i.strip() for i in mylines if len(i.strip()) > 0]
    big_list = []
    for i in range(0, len(mylines), num_of_fields):
        mydict = {}
        for j in range(num_of_fields):
            elem = mylines[i + j]
            mydict = key_value(elem, mydict)
        big_list.append(mydict)
    return big_list

def convert_direction_to_integer(the_direction):
    if not the_direction.lower() in ["down", "up", "right", "left"]:
        raise ValueError("I don't recognize this: {}".format(the_direction))
    the_direction = the_direction.lower()
    myint = ""
    if the_direction == "up":
        myint = 90
    elif the_direction == "down":
        myint = -90
    elif the_direction == "right":
        myint = 0
    elif the_direction == "left":
        myint = 180
    else:
        s = "This was not found: {}".format(the_direction)
        raise ValueError(s)
    return myint

def PosicionPlayerMap(filepath):
    with open(filepath, "r") as f:
        mylines = f.readlines()
        mylines = [i.strip() for i in mylines if len(i.strip()) > 0]
    big_list = []
    for i, line in enumerate(mylines):
        for j, element in enumerate(line):
            # print(i, j, element)
            if element == "p":
                return j, i
    raise ValueError("Player not found!")


def objetiveposicionmap():
    x, y = -1, -1
    filepath = os.path.join("data", constants.MAPA)
    with open(filepath, "r") as f:
        mytiles = f.readlines()
        mytiles = [i.strip() for i in mytiles if len(i.strip()) > 0]
    for col, tiles in enumerate(mytiles):
        for row, tile in enumerate(tiles):
            if tile == 'O':
                x = row
                y = col
    return x, y


