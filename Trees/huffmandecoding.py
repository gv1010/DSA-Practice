def decodeHuff(root, s):
	#Enter Your Code Here
    list1 = list(s)
    step = 0
    node = root
    while node.data == root.data :
        #print(1)
        #print(node.freq)
        if int(list1[step]) == 0:
            node = node.left
            if node.data == root.data:
                step = step + 1
            else:
                print(node.data, end= "")
                step = step + 1
                node = root
        else:
            node = node.right
            if node.data == root.data:
                step = step + 1
            else:
                print(node.data, end= "")
                step = step + 1
                node = root

        if step == len(list1):
            break