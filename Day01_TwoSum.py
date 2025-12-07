# LeetCode 1: Two Sum
# Brute-force solution (O(n^2))

class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        
        # Check every pair of numbers
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []  # No valid pair found


# Example run
if __name__ == "__main__":
    obj = Solution()
    nums = [1, 2, 3, 4]
    target = 8
    output = obj.twoSum(nums, target)
    print(output)  # Output: []
