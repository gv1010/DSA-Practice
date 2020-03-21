from collections import defaultdict
class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = defaultdict(list)
		self.reverse = defaultdict(list)
		self.visited = None
		self.scc_list = []
		self.comp = []
		self.stack = []
	def addEdge(self, u,v):
		self.graph[u].append(v)
	def dfs(self, s):
		self.visited[s] = True
		for i in self.graph[s]:
			if self.visited[i] == False:
				self.dfs(i)
		self.stack.append(s)
	def dfsUtil(self):
		self.visited = [False]*self.vertices
		for i in list(self.graph.keys()):
			if self.visited[i] == False:
				self.dfs(i)
	def reverseConnections(self):
		for i in list(self.graph.keys()):
			for j in self.graph[i]:
				self.reverse[j].append(i)
	def stackDfs(self,node):
		if self.visited[node] == False:
			self.visited[node] = True
			self.comp.append(node)
		for i in self.reverse[node]:
			if self.visited[i] == False:
				self.stackDfs(i)
			
		#return self.comp
	def stackDfsUtil(self):
		self.visited = [False]*self.vertices
		for i in list(self.reverse.keys()):
			self.comp = []
			if self.visited[i] == False:
				self.stackDfs(i)
			if self.comp != []:
				self.scc_list.append(self.comp)
		
	def run(self):
		self.dfsUtil()
		print('forward -- ', self.graph)
		self.reverseConnections()
		print('reverse -- ', self.reverse)
		self.stackDfsUtil()
		return self.scc_list
		
g =Graph(8)
#g.addEdge(0,2)
#g.addEdge(0,3)
#g.addEdge(1,0)
#g.addEdge(2,1)
#g.addEdge(3,4)

#g.addEdge(0,1)
#g.addEdge(1,2)
#g.addEdge(2,3)
#g.addEdge(2,4)
#g.addEdge(3,0)
#g.addEdge(4,2)

g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,1)
g.addEdge(1,4)
g.addEdge(4,5)
g.addEdge(5,6)
g.addEdge(6,7)
g.addEdge(7,5)



print(g.run())

		