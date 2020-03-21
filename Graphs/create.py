from collections import defaultdict 
  
# function for adding edge to graph 
#graph = defaultdict(list) 
def addEdge(graph,u,v): 
	graph[u].append(v) 

# definition of function 
def generate_edges(graph): 
	edges = [] 

	# for each node in graph 
	for node in graph: 
		  
		# for each neighbour node of a single node 
		for neighbour in graph[node]: 
			  
			# if edge exists then append 
			edges.append((node, neighbour)) 
	return edges

#addEdge(graph,'a','c') 
#addEdge(graph,'b','c') 
#addEdge(graph,'b','e') 
#addEdge(graph,'c','d') 
#addEdge(graph,'c','e') 
#addEdge(graph,'c','a') 
#addEdge(graph,'c','b') 
#addEdge(graph,'e','b') 
#addEdge(graph,'d','c') 
#addEdge(graph,'e','c') 
#  
# Driver Function call  
# to print generated graph 
#print(generate_edges(graph))
#print(graph)

def bfs(node):
	V = [0]*(len(graph) + 1)
	q = []
	q.append(node)
	V[node] = 1
	while q:
		node = q.pop(0)
		print(node, end = " ")
		for i in graph[node]:
			if V[i] == 0:
				q.append(i)
				V[i] = 1
	return V
				
#addEdge(graph, 1,2)
#addEdge(graph, 2,1)
#addEdge(graph, 1,3)
#addEdge(graph, 3,1)			
#addEdge(graph, 2,4)
#addEdge(graph, 4,2)
#addEdge(graph, 3,4)
#addEdge(graph, 4,3)
#addEdge(graph, 3,5)
#addEdge(graph, 5,3)
#addEdge(graph, 5,4)
#addEdge(graph, 4,5)			
#addEdge(graph, 5,6)
#addEdge(graph, 6,5)
#print(graph)
#print(bfs(2))
graph = { 
		  1: [2,3],
		  2: [1,4,5],
		  3: [1,4],
		  4: [3,2,5],
		  5: [4,2,6],
		  6: [5,7],
		  7: [6] 
		}
		 
V = [0]*(len(graph)+1)
def dfs(node):
	V[node] = 1
	for i in graph[node]:
		if V[i] == 0 :
			print(i, end = " ")
			dfs(i)
			
print(1, end = " ")
(dfs(1))	