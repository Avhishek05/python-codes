from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
        
    def dfsutil(self,visited,s):
        visited[s]=True
        print(s,end=" ")
        for i in self.graph[s]:
            if visited[i]==False:
                self.dfsutil(visited,i)

                
    def dfs(self,s):
        visited=[False]*(len(self.graph))
        self.dfsutil(visited,s)
        
g= Graph()
g.addedge(0, 1)
g.addedge(0, 2)
g.addedge(1, 2)
g.addedge(2, 0)
g.addedge(2, 3)
g.addedge(3, 3)
g.dfs(2)
