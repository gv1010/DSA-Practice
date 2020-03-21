from collections import defaultdict
graph = defaultdict(list)

def addEdge(graph, u, v):
	graph[u].append(v)
	
def dfs(s,graph):
	stack = []
	stack.append(s)
	vis = [0]*(len(graph))
	reVis = [0]*(len(graph))
	flag = False
	while len(stack):
	
		s = stack.pop(-1)
		if not vis[s]:
			#print(s, end = " ")
			vis[s] = 1
		
			
		for node in graph[s]:
			if not vis[node]:
				stack.append(node)
			else:
				#falg = True
				reVis[node] = reVis[node] + 1
	#print(reVis)
	if sum(reVis) >= 1:
		return True
	else:
		return False
				
#graph = Graph(4) 
addEdge(graph,0, 1) 
addEdge(graph,0, 2) 
addEdge(graph,1, 2) 
addEdge(graph,2, 0) 
addEdge(graph,2, 3) 
addEdge(graph,3, 3) 
			
#graph = {
#			0: [1],
#			1: [2,3],
#			2: [4],
#			3: [6],
#			4: [6,5],
#			5: [8],
#			6: [7],
#			7: [5],
#		    8: [1]
#		}

#graph = {0:[0,1],1:[]}
print(dfs(0, graph))
#print(graph[2])
	