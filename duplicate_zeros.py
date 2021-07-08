# def duplicateZeros(arr):

x=[1,0,2,3,0,4,5,0]
for i in range(0,len(x)):
	if x[i]==0:
		x.insert(x[i]+1,0)
	else:
		x=x
print(x)