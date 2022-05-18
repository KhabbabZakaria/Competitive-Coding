#Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#leetcode problem 7. Medium Level

class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            string = str(x)
            string = string[::-1]
            x = int(string)
        else:
            string = str(x*(-1))
            string = string[::-1]
            x = int(string)
            x = x*(-1)
        if x in range(-2**31, 2**31 - 1):
            return x
        else:
            return 0


