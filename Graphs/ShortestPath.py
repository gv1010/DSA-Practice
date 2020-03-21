from collections import defaultdict 
graph = defaultdict(list)
def addEdge(graph, u, v):
	graph[u].append(v)


def ShortestPath(src, graph):
	past = [src]
	cur = []
	dist = {}
	dist[src] = 0
	while past != []:
		for node in past:
			for neigh in graph[node]:
				if neigh not in dist:
					dist[neigh] = dist[node] + 1
					cur.append(neigh)
			past = cur
			cur = []
		return dist

addEdge(graph, 1,2)
addEdge(graph, 1,3)
addEdge(graph, 2,1)
addEdge(graph, 2,4)			
addEdge(graph, 3,1)
addEdge(graph, 3,4)
addEdge(graph, 3,7)
addEdge(graph, 4,2)
addEdge(graph, 4,3)
addEdge(graph, 4,5)
addEdge(graph, 5,4)
addEdge(graph, 5,6)			
addEdge(graph, 6,5)
addEdge(graph, 6,7)
addEdge(graph, 7,6)
addEdge(graph, 7,3)
print(graph)
print(ShortestPath(1, graph))