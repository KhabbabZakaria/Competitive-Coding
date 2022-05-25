class Solution:
    def intToRoman(self, num):
        result = ''
        num_str = str(num)
        if len(num_str)>3:
            thousands = num_str[0]

            for _ in range(int(num_str[0])):
                result = result + 'M'
            num_str = num_str[1:]
        
        if len(num_str)>2:
            hundreds = num_str[0]
            if int(hundreds)<4:
                for _ in range(int(hundreds)):
                    result = result + 'C'
            if int(hundreds) == 4:
                result = result + 'CD'
            if int(hundreds) == 5:
                result = result + 'D'
            if int(hundreds) >5 and int(hundreds) <9:
                result = result + 'D'
                for _ in range(int(hundreds)-5):
                    result = result + 'C'
            if int(hundreds) == 9:
                result = result + 'CM'
             
            num_str = num_str[1:]

        if len(num_str)>1:
            tens = num_str[0]
            if int(tens)<4:
                for _ in range(int(tens)):
                    result = result + 'X'
            if int(tens) == 4:
                result = result + 'XL'
            if int(tens) == 5:
                result = result + 'L'
            if int(tens) >5 and int(tens) <9:
                result = result + 'L'
                for _ in range(int(tens)-5):
                    result = result + 'X'
            if int(tens) == 9:
                result = result + 'XC'
             
            num_str = num_str[1:]

        if len(num_str)>0:
            ones = num_str[0]
            if int(ones)<4:
                for _ in range(int(ones)):
                    result = result + 'I'
            if int(ones) == 4:
                result = result + 'IV'
            if int(ones) == 5:
                result = result + 'V'
            if int(ones) >5 and int(ones) <9:
                result = result + 'V'
                for _ in range(int(ones)-5):
                    result = result + 'I'
            if int(ones) == 9:
                result = result + 'IX'
             
        return result

sol = Solution()
x = sol.intToRoman(1994)

print(x)