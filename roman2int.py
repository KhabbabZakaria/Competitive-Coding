class Solution:
    def romanToInt(self, s):
        mylist = list(s)
        mydict = {'I':1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        i = 0
        while i<len(mylist)-1:
            if mydict[mylist[i]] >= mydict[mylist[i+1]]:
                result = result + mydict[mylist[i]]
                i = i + 1
            else:
                result = result + (mydict[mylist[i+1]] - mydict[mylist[i]])
                i = i +2

        if len(mylist)>1:
            if mydict[mylist[-2]] >= mydict[mylist[-1]]:
                result = result + mydict[mylist[-1]]

        if len(mylist)==1:
            return mydict[mylist[-1]]

        return result

sol = Solution()

x = sol.romanToInt("D")

print(x)