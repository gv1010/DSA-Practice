from collections import defaultdict
class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
		self.visited = None
	def addEdge(self, u,v):
		self.graph[u].append(v)

	def dfs(self,s):
		
		self.stack = [s]
		while len(self.stack):
			s = self.stack.pop()
			if self.visited[s] == 0:
				self.visited[s] = 1
				print(s, end = "-")
			for node in self.graph[s]:
				if self.visited[node] == 0:
					self.stack.append(node)
					
	def dfsUtil(self):
		self.visited = len(self.graph)*[0]
		for node in self.graph:
			if self.visited[node] == 0:
				self.dfs(node)
g = Graph()
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(3,4)
g.addEdge(4,1)
g.dfsUtil()

			
	