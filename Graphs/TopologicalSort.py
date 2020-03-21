from collections import defaultdict
class Graph:
	def __init__(self, vertices):
		self.graph = defaultdict(list)
		self.visited = None
		self.vertices = vertices
		self.topologicalOrder = []
	def addEdge(self, u, v):
		self.graph[u].append(v)
	def topologicalSort(self,s):
		if self.visited[s] == 0:
			self.visited[s] = 1
		for i in self.graph[s]:
			if self.visited[i] == 0:
				self.topologicalSort(i)
		self.topologicalOrder.insert(0,s)
	#def iterTopologicalSort(self,s):
		
	def topUtil(self):
		self.visited = [0]*self.vertices
		print(self.graph)
		for i in sorted(self.graph.keys()):
			if self.visited[i] == 0:
				self.topologicalSort(i)
		print(self.topologicalOrder)
		
g = Graph(6)
g.addEdge(5,0)
g.addEdge(5,2)
g.addEdge(4,0)
g.addEdge(4,1)
g.addEdge(2,3)
g.addEdge(3,1)
g.addEdge(3,5)
g.topUtil()

