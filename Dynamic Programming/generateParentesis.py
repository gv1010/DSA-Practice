def generate(n):
	res = []
	def genePara(S = "", left = n, right = n):
		if len(S) == 2*n:
			res.append(S)
		if left > 0:
			genePara(S+"(", left-1, right)
		if left < right:
			genePara(S+")", left, right-1)
	genePara()
	return (res)
n = 4
print(generate(n))
		
    node = root
    p = n1
    q = n2
    while node:
        if p == node.key or q == node.key:
            return node.key
        if (p < node.key < q) or (p > node.key > q):
            return node.key
        if p < node.key and q < node.key:
            node = node.left
        if p > node.key and q > node.key:
            node = node.right
		