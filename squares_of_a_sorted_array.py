# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

def sortedSquares(nums):
	res=[]
	for i in nums:
		x=i**2
		res.append(x)
	return sorted(res)

print(sortedSquares([-4,-1,0,3,10]))

#sample solution

# def sortedSquares(self, nums: List[int]) -> List[int]:
#          return sorted([x*x for x in nums])

#solution 2

# def sortedSquares(self, nums: List[int]) -> List[int]:
#         return sorted(list(map(lambda x: x * x, nums)))