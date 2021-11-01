class ModNGroup:

    def __init__(self, n):
        self.x = list(range(0, n))

    def validateIndex(self, index):
        if index < 0 or index >= len(self.x):
            raise Exception(f'invalid index : {index}')

    def additionOnGroup(self, index1, index2):
        self.validateIndex(index1)
        self.validateIndex(index2)
        return (self.x[index1] + self.x[index2]) % len(self.x)

    def getIdentity(self):
        return self.x[0]

    def getInverse(self,index):
        self.validateIndex(index)
        return len(self.x)-index


def printModGroupElements(n):
    g1 = ModNGroup(n)
    print(g1.x)


def printAdditionInGroup(n, index1, index2):
    g1 = ModNGroup(n)
    print(g1.additionOnGroup(index1, index2))


def printIdentity(n):
    g1 = ModNGroup(n)
    print(g1.getIdentity())

def printInverse(n,index):
    g1 = ModNGroup(n)
    print(g1.getInverse(index))

def printGroupAndIdentity(n):
    g1=ModNGroup(n)
    print(g1.x, "," ,g1.getIdentity())

printModGroupElements(2)
printIdentity(2)
printInverse(2,0)
printGroupAndIdentity(2)
