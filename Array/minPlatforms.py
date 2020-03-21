#for _ in range(int(input())):
#n = int(input())
#arr1 = list(map(str, input().rstrip().split()))
#arr2 = list(map(str, input().rstrip().split()))
arr1 = [900,940,950,1100,1500,1800]
arr2 = [910,1200,1120,1130,1900,2000]
sch = []
for i in range(len(arr1)):
	sch.append((arr1[i], arr2[i]))
sch = sorted(sch, key = lambda x:x[0])
print(sch)
platform = [sch[0]]
max_plot = float('-inf')
for x,y in sch[1:]:
	platform = sorted(platform, key= lambda x:x[1])
	i = 0
	print(platform)
	for x1,y1 in platform:
		print(platform)
		if x <= y1:
			platform.append((x,y))
		if x > y1:
			platform.pop(i)
			platform.append((x,y))
		max_plot = max(len(platform), max_plot)	
		i=i+1
print(max_plot)
	
#arr1 = [0900,0940,0950,1100,1500,1800]
#arr2 = [0910,1200,1120,1130,1900,2000]
		
	
		
		
		
	