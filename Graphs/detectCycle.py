from collections import defaultdict
class Graph:
	def __init__(self, vertices):
		self.graph = defaultdict(list)
		self.visited = None
		self.vertices = vertices
		
	def addEdge(self, u, v):
		self.graph[u].append(v)
		
	def dfs(self, s):
		self.visited[s] = True
		self.record[s] = True
		for i in self.graph[s]:
			if self.visited[i] == False:
				if self.dfs(i) == True:
					return True
			elif self.record[i] == True:
				return True
		self.record[s] = False	
		return False
		
	def dfsUtil(self):
		self.visited = [False]*self.vertices
		self.record = [False]*self.vertices
		for i in list(self.graph.keys()):
			if self.visited[i] == False:
				if self.dfs(i) == True:
					return True
		return False

g = Graph(3)

g.addEdge(1,0) 
g.addEdge(2,0) 
g.addEdge(2,1) 

#g.addEdge(2, 3) 
#g.addEdge(3, 4) 
#g.addEdge(5, 1) 
#g.addEdge(4, 5)

if g.dfsUtil() == False:
	print("No cycle")
else:
	print("Graph has cycle")
					