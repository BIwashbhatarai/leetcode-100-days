class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1 , n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
    
obj = Solution()
nums = [1,2,3,4]
target = 8
output = obj.twoSum(nums,target)
print(output)