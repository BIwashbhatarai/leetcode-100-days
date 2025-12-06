class Solution(object):
    def plusOne(self, digits):
        n = int(''.join(map(str, digits)))
        n += 1
        arr = [int(d) for d in str(n)]
        return arr
obj = Solution()
print(obj.plusOne([1,2,3]))