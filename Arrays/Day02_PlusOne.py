# LeetCode 66: Plus One
# Convert digits to integer, add one, convert back to list

class Solution(object):
    def plusOne(self, digits):
        # Convert list of digits to integer
        n = int(''.join(map(str, digits)))
        
        # Add one
        n += 1
        
        # Convert back to list of digits
        arr = [int(d) for d in str(n)]
        return arr


# Example run
if __name__ == "__main__":
    obj = Solution()
    print(obj.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
