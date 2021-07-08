# Find Numbers with Even Number of Digits

# Example 1:

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.
# Example 2:

# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.
#  

def findNumbers(nums):
	st=[]
	res=0
	for i in nums:
		st.append(str(i))
	for i in st:
		if len(i)%2==0:
			res+=1
	print(res)

findNumbers([12,345,2,6,7896])
findNumbers([555,901,482,1771])

# #solutin 1 

# class Solution(object):
#     def findNumbers(self, nums):
#         return reduce(lambda x,y: x+y,map(lambda x: 0 if len(x)%2 else 1, map(lambda x: str(x), nums)))

# #solution 2

# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
        
#         counter = 0
        
#         for number in nums:
            
#             if len( str(number) ) % 2 == 0:
                
#                 counter += 1
                
#         return counter

