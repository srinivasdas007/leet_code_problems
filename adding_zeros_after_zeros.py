# In this problem we are adding zeros to the array if it consists of zeros.

# x=[1,0,2,3,0,4,5,0]
# result=[]

# ins=False

# l=len(x)

# c=range(5)

# print(c)

# for i in range(0,l+2):
# 	if ins==True:
# 		ins=False
# 		continue
# 	if x[i]==0:
# 		x.insert(i+1,0)
# 		l=l+1
# 		ins=True
# 	print(i+1)

# print(x)
x=[1,0,2,3,0,4,5,0]
i=0
flag=False
while i<len(x):
	if flag==True:
		flag=False
		i=i+1
		continue
	elif x[i]==0:
		x.insert(i+1,0)
		flag=True# we have inserted 1 0 so we have to notify while loop about the increse of length
	i=i+1

print(x)
