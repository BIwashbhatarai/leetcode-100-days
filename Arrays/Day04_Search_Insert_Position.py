# LeetCode 35: Search Insert Position
# Binary Search | Time: O(log n), Space: O(1)


class Solution(object):
    def searchInsert(self, nums, target):
        """
        Returns the index of the target if found.
        Otherwise, returns the index where it should be inserted.
        """
        left = 0
        right = len(nums) - 1

        # Binary search loop
        while left <= right:
            mid = (left + right) // 2

            # If target found
            if nums[mid] == target:
                return mid

            # If target is greater, search right half
            elif nums[mid] < target:
                left = mid + 1

            # If target is smaller, search left half
            else:
                right = mid - 1

        # Target not found → left = correct insertion index
        return left


# Example usage:
obj = Solution()
print(obj.searchInsert([1, 2, 4], 3))  # Output: 2
