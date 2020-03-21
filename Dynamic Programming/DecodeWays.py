count = [0]
from collections import defaultdict
store = {}
def decode(S, store):
	if S == "":
		return 1
	if S[0] == "0":
		return 0
	if S in store.keys():
		return store[S]
	result = decode(S[1:], store)
	if len(S)>= 2 and int(S[:2] if len(S)>2 else S) <= 26:
		result += decode(S[2:], store)
	store[S] = result
	return result	
		
S = "91999"
print(decode(S, store))
