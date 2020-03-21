def rectangle(A,B,C,D,E,F,G,H):
	#rect1 = (A,B) --- (C,D)
	#rect2 = (E,F) --- (G,H)
	rect1 = [(A,B), (C,D)]
	rect2 = [(E,F), (G,H)]
	rect1 = sorted(rect1, key = lambda x: x[0])
	rect2 = sorted(rect2, key = lambda x: x[0])
	def func(rect1, rect2):
		A, B = rect1[0]
		C, D = rect1[1]
		E, F = rect2[0]
		G, H = rect2[1]
		res = []
		if E <= A <= G and F<= B <= H:
			res.append([A,B])
		if E <= C <= G and F<= B <= H:
			res.append([C,B])
		if E <= A <= G and F<= D <= H:
			res.append([A,D])
		if E <= C <= G and F<= D <= H:
			res.append([C,D])
		return res
	if A == C and B == D:
		return abs(E-G)*abs(F-H)
	if E == G and F == H:
		return abs(A-C)*abs(B-D)
	res1 = func(rect1, rect2)
	res2 = func(rect2, rect1)
	if len(res1) + len(res2) == 2:
		area = abs(res1[0][0]-res2[0][0]) * abs(res1[0][1]-res2[0][1])
		return abs(A-C)*abs(B-D) + abs(E-G)*abs(F-H) - area
	elif len(res1) == 4:
		return abs(A-C)*abs(B-D)
	elif len(res2) == 4:
		return abs(E-G)*abs(F-H)
	else:
		return abs(A-C)*abs(B-D) + abs(E-G)*abs(F-H)
A = -3
B = 0 
C = 3
D = 4
E = -3
F = 0 
G = 3
H = 6


A = -2
B = -2
C = 2
D = 2
E = 3
F = 3
G = 4
H = 4 

A = 0
B = 0
C = 0
D = 0
E = -1
F = -1
G = 1
H = 1
print(rectangle(A,B,C,D,E,F,G,H))