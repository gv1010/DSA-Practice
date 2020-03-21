from collections import defaultdict
class Graph:
	def __init__(self,vertices):
		self.vertices = vertices
		self.graph = defaultdict(list)
		self.queue = [float('inf')]*(self.vertices+1)
		self.shortest = [False] * (self.vertices+1)
		self.path = []
		for i in list(self.graph.keys()):
			self.queue[i] = [float('inf')]
		
	def dijkstras(self,source,weight):
		self.queue[source] = 0
		#while self.queue != []:
		for _ in range(self.vertices):
			min_dist = min(self.queue)
			u = self.queue.index(min_dist)
			#self.queue.pop(u)
			self.shortest[u] = True
			self.path.append([u,min_dist])
			for i in range(len(self.graph[u])):
				if self.queue[i+1] > self.queue[u] + weight[i][u] and self.shortest[i+1] == False and self.graph[u][i] > 0:
					self.queue[i+1] = self.queue[u] + weight[i][u]
		print(self.path)
			
weight =[
		[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]
g = Graph(9)
g.dijkstras(1,weight)
