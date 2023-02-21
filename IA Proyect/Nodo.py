class Node:

    def __init__(self, key, p, parent):
        self.key = key
        self.p = p
        self.parent = parent

    def getKey(self):
        return self.key

    def setP(self, p):
        self.p = p

    def getP(self):
        return self.p

    def getParent(self):
        return self.parent

#nodo = Node([1,2,3], [1,1], None)
#print(nodo.getKey())
