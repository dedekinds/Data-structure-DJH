邓俊辉-数据结构-30240184_06-B1-5 带权图
带权图的一种实现

class Vertex(object):
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):#连接对象的顶点类
        return self.connectedTo.keys()

    def getId(self):#自己的ID
        return self.id

    def getWeight(self,nbr):#权重
        return self.connectedTo[nbr]


class Graph(object):
    def __init__(self):
        self.vertList = {}#顶点集合
        self.numVertices = 0#顶点数

    def addVertex(self,key):#增加一个顶点
        self.numVertices = self.numVertices + 1#顶点数+1
        newVertex = Vertex(key)#创建一个新的顶点类
        self.vertList[key] = newVertex#加入顶点集合
        return newVertex

    def getVertex(self,n):#找某个顶点
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):#g.addEdge(起始点,终点,权重)
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()#print(g.getVertices())求顶点

    def __iter__(self):
        return iter(self.vertList.values())



g=Graph()
for i in range(6):
    g.addVertex(i)
print(g.vertList)

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))
