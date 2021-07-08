def findErrorNums(nums):
	y={}
	for i in nums:
		if i in y:
			y[i]+=1
		else:
			y[i]=1
	# return y
	for k,v in y.items():
		if v==2:
			c=k-1
			if c==k:
				return [k,k+1]
			else:
				return [c,k]
			# return c
			# if c==k:
			# 	return [k,k+1]
			# else:
			# 	return [k-1,k]

	# for k,v in y.items():
	# 	if y[v]==2:
	# 		return y

print(findErrorNums([1,2,2,4]))
print(findErrorNums([1,1]))
print(findErrorNums([2,2]))