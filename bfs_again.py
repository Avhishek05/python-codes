from collections import defaultdict
class Graph:
	def __init__(self,size):
		self.graph = defaultdict(list)
		self.size=size
	def addedge(self,u,v):
		self.graph[u].append(v)

	def bfs(self,s):
		visited=[False]*(self.size)
		print(len(self.graph))
		queue =[]
		queue.append(s)
		visited[s]=True

		while queue:
			a=queue.pop()
			print(a,end =" ")
			for i in self.graph:
				if visited[i]==False:
					queue.append(i)
					visited[i]=True
g= Graph(6)
g.addedge(1, 2)
g.addedge(1, 3)
g.addedge(1, 4)
g.addedge(3, 5)
g.addedge(4, 6)
g.addedge(6, 7)


g.bfs(1)