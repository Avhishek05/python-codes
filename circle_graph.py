from collections import defaultdict
class Graph():
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
                  
    def iscycleutil(self,v,visited,restack):
        visited[v]=True
        restack[v]=True
        for j in self.graph[v]:
            if visited[j]==False:
                if self.iscycleutil(j,visited,restack)==True:
                    return True
            elif restack[j]==True:
                return True
        restack[v]=False
        return False
        
    def dfs(self):
        visited=[False]*(self.V)
        restack=[False]*(self.V)
        for i in range(self.V):
            if visited[i]==False:
                if self.iscycleutil(i,visited,restack)==True:
                    return True
                return False

g= Graph(4)
g.addedge(0, 1)
g.addedge(0, 2)
g.addedge(1, 2)
g.addedge(2, 0)
g.addedge(2, 3)
g.addedge(3, 3)
if g.dfs()==1:
    print("cycle")
else:
    print("no cycle")
