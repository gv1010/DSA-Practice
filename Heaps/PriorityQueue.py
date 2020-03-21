# priority queue implementation from hackerearth
class PriorityQ:
	def __init__(self, arr):
		self.arr = [0]+arr
	def heapify(self,i):
		left = 2*i
		right = 2*i+1
		if left < len(self.arr) and self.arr[i] < self.arr[left] :
			largest = left
		else:
			largest = i
		if right < len(self.arr) and self.arr[right] > self.arr[largest]:
			largest = right
		if largest != i:
			self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
			self.heapify(largest)
		
	def heapify_util(self):
		for i in range(len(self.arr)//2,0,-1):
			self.heapify(i)
		return self.arr
		
	def insertQ(self, ele):
		self.arr.append(ele)
		self.heapify_util()
		print(self.arr)
	def pop_max(self):
		temp = self.arr[1]
		self.arr[1] = self.arr[-1]
		self.arr.pop()
		self.heapify_util()
		return temp
		
	def pop_min(self):
		return self.arr.pop()

arr = [1,2,3,4,5,6,7,8]
pq = PriorityQ(arr)
print(pq.heapify_util())
#pq.insertQ(4)
pq.insertQ(7)
print(pq.pop_max())
print(pq.pop_max())
print(pq.pop_max())
print(pq.pop_max())
print(pq.pop_max())
print(pq.pop_min())
print(pq.heapify_util())

		
		