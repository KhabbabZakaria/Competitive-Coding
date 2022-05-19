class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        c = a+b
        return str(format(c, 'b'))


sol = Solution()
a = "11" 
b = "1" 
x = sol.addBinary(a,b)


print(x)

