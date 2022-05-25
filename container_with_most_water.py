
class Solution:
    def maxArea(self, height):
        result = 0
        L = 0
        R = len(height) - 1

        while R>L:
            distance = (R - L)
            result_new = distance*min(height[L], height[R])
            if result_new>result:
                result = result_new
            if height[L] > height[R]:
                R = R - 1
            else:
                L = L + 1
        return result

sol = Solution()
x = sol.maxArea([1,1])
print(x)
        
