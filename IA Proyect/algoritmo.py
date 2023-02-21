import os
import constants
import numpy as np
from os import stat
from Nodo import Node

from os import stat
from Nodo import Node

def createCopy(status):
    parent = status
    status = status.getKey()
    copy = []
    for row in status:
        rowCopy = []
        for element in row:
            rowCopy.append(element)
        copy.append(rowCopy)        
    return Node(copy, None, parent)

def getPlayerLocation(status):
    status = status.getKey()
    for i in range(len(status)):
        for j in range(len(status[i])):
            if status[i][j] == "p":
                return i, j                           
    
def generateChilds(status):    
    row, column =  getPlayerLocation(status)
    print("Row:" + str(row) + ",Column:" + str(column))
    status.setP([row, column])
    childs = []
    #up
    try:
        if status.getKey()[row - 1][column] == "x":
            newStatus = createCopy(status)
            newStatus.getKey()[row][column] = "x"
            newStatus.getKey()[row - 1][column] = "p"
            childs.append(newStatus)            
    except:
        pass
    #right
    try:
        if status.getKey()[row][column+1] == "x":
            newStatus = createCopy(status)
            newStatus.getKey()[row][column] = "x"
            newStatus.getKey()[row][column+1] = "p"
            childs.append(newStatus)            
    except:
        pass
    #down
    try:
        if status.getKey()[row + 1][column] == "x":
            newStatus = createCopy(status)
            newStatus.getKey()[row][column] = "x"
            newStatus.getKey()[row + 1][column] = "p"
            childs.append(newStatus)            
    except:
        pass
    #left
    try:
        if status.getKey()[row][column-1] == "x":
            newStatus = createCopy(status)
            newStatus.getKey()[row][column] = "x"
            newStatus.getKey()[row][column-1] = "p"
            childs.append(newStatus)            
    except:
        pass
    return childs

def arbol1(status,mx,my):
    goal = [my, mx]

    l = [status]
    finalStatus = createCopy(status)
    row, column = getPlayerLocation(finalStatus)
    finalStatus.getKey()[row][column] = "x"
    finalStatus.getKey()[goal[0]][goal[1]] = "p"
    l2 = [finalStatus]

    printList(l, "-")
    printList(l2, "*")  
    for i in range(50):
        newList = []
        for s in l:            
            newList = newList + generateChilds(s)
        l = newList
        printList(l, "-")
        #comparar con la lista2
        for s1 in l:
            for s2 in l2:
                if s1.getKey() == s2.getKey():
                    #en caso positivo, break                    
                    return buildPath(s1, s2,status)
        #en caso negativo generar nuevos hijos para l2
        newList2 = []
        for s in l2:
            newList2 = newList2 + generateChilds(s)
        l2 = newList2
        printList(l2, "*")
        #comparar el nuevo l2 con el l1
        for s1 in l:
            for s2 in l2:
                if s1.getKey() == s2.getKey():
                    #en caso positivo, break                    
                    return buildPath(s1, s2,status)
        #en caso negativo se deja que continue el for

def printList(l, sep):
    print(sep*10)
    for m in l:
        print(*m.getKey(), sep="\n")
        print("\n")

def buildPath(n1, n2,status):
    print("Encontrado")
    printList([n1], "1")

    path1 = []
    current = n1
    while current != None:
        path1 = [current.getP()] + path1
        current = current.getParent()

    path2 = []
    current = n2
    while current != None:
        path2.append(current.getP())
        current = current.getParent()

    printList([status], "%")
    print(path1, path2)
    row, column = getPlayerLocation(n1)
    final = path1[:-1] + [[row, column]] + path2[1:-1]
    #print(final)
    return final

    #n1 el nodo del arbol que va desde inicio a meta
    #n2 el nodo del arbol que va desde la meta hasta el inicio

class BFSMatriz:
   def __init__(self,x,y,mx,my):
            self.coordenadas = []
            self.x = x
            self.y = y          
            self.mx = mx
            self.my = my
            print("X:" + str(x))
            print("Y:" + str(y))
            matriz = []
            filepath = os.path.join("data", constants.MAPA)
            with open(filepath, "r") as f:
                mytiles = f.readlines()
                mytiles = [i.strip() for i in mytiles]

            for col, tiles in enumerate(mytiles):
                 for row, tile in enumerate(tiles):
                        if tile == 'm' or tile == 'L' or tile == 'B':
                            mybloque = 0
                            matriz.append(mybloque)                
                        if  tile == '.':
                            mybloque = "x"
                            matriz.append(mybloque)                
                        if tile == 'T':
                            mybloque = "x"
                            matriz.append(mybloque)
                        if tile == 'p':
                            mybloque = "p"
                            matriz.append(mybloque)                           
                        if tile == 'O':
                            mybloque = "x"
                            matriz.append(mybloque)                

            amatriz = np.array(matriz).reshape(-1,8)
            status  = Node(amatriz.tolist(),[y,x], None)

            #finalStatus.getKey()
            camino = arbol1(status,self.mx,self.my)
            for coordenada in camino:
                self.coordenadas.append(coordenada)                
                print(coordenada[0], coordenada[1])

   def __getitem__(self, item):
        return self.coordenadas[item]


            
               

