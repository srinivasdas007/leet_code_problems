def merge(nums1,nums2,m,n):
	num1=nums1[:m]
	return sorted(num1+nums2)
print(merge([1,2,3,0,0,0],[2,5,6],3,3))



# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6],
# n = 3

# n1=nums1[:m]
# print(n1)
# n=n1.extend([9,9,2])

# print(n)