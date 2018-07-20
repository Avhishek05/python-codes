from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)


    def dfsutil(self,s,visited):
        visited[s]=True
        for i in self.graph[s]:
            if visited[i]==False:
                self.dfsutil(i,visited)
        
        if visited[s]==False:
            dfsutil(self)
    def findmothervertex(self):
        visited=[False]*(self.V)
        v=0 #to store visited node
        for i in range(self.V):
            if visited[i]==False:
                self.dfsutil(i,visited)
                v=i
        visited =[False]*(self.V)
        self.dfsutil(v,visited)
        if any(i==False for i in visited):
            return -1
        else:
            return v
            
                
g=Graph(7)
g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,3)
g.addedge(4,1)
g.addedge(6,4)
g.addedge(5,6)
g.addedge(5,2)
g.addedge(6,0)
print(g.findmothervertex())
