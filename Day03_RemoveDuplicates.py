# LeetCode 26: Remove Duplicates from Sorted Array
# Two-pointer approach (in-place)

class Solution(object):
    def removeDuplicates(self, nums):
        # Pointer i tracks the position of the last unique element
        i = 0
        
        # Pointer j scans through the array
        for j in range(len(nums)):
            # When a new unique value is found
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1


# Example run
if __name__ == "__main__":
    obj = Solution()
    print(obj.removeDuplicates([1,1,2,3,3]))  # Output: 3
