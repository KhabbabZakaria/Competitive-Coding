class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        s_list = []
        first_space = True
        for i in range(len(s)):
            if s[i] == ' ' and first_space ==  True:
                pass
            if s[i] == ' ' and first_space == False:
                break
            if s[i] != ' ':
                s_list.append(s[i])
                first_space = False

        s = ''.join(str(e) for e in s_list)
        

        s=s.replace(" ", "")
        if len(s) == 0:
            return 0
        if s[0] == '+' or s[0] == '-':
            integers = []
            for j in range(1, len(s)):
                try:
                    i = int(s[j])
                    integers.append(s[j])
                except:
                    break
            if len(integers) == 0:
                return 0
            integer = int(''.join(str(e) for e in integers))
            if s[0]=='-' and (-1)*integer < -2**31:
                return -2**31
            if s[0]=='+' and integer > 2**31 - 1:
                return 2**31 - 1
            if s[0] == '+':
                return integer
            else:
                return integer*(-1)
        else:
            integers = []
            for j in range(0, len(s)):
                try:
                    i = int(s[j])
                    integers.append(s[j])
                except:
                    break
            if len(integers) == 0:
                return 0
            integer = int(''.join(str(e) for e in integers))
            if integer > 2**31 - 1:
                integer = 2**31 - 1
            return integer



sol = Solution()
s = "   +0 123"
x = sol.myAtoi(s)
print(x)