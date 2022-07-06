#bottom up
#climbing stairs
#order not important
#example: upmost = 3; possible jumps = 1,2. ways = 1+1+1, 2+1, 1+2
def numberOfWaysToMakeChange(n, jumps):
    # Write your code here.
    #pass
    jumps.sort()
    dp = [0]*(n+1)
    dp[-1] = 1
    for i in reversed(range(n)):
        diff = n - i
        possibilities = []
        for j in jumps:
            if j<=diff:
                possibilities.append(j)
            else:
                break
        for k in possibilities:
            dp[i] += dp[i+k]
    return dp[0]




#top down
#coin problem
#order important
#example: target amount = 10; coin denominations = [1,5,10,25]. ways= 1coin x 10times, 5coins x 2times,
#(1coin x 5times + 5coin x 1times), 10coin x 1times. But (5coin x 1times + 1coin x 5times) is not an option 
# as (1coin x 5times + 5coin x 1times) is already there.
def numberOfWaysToMakeChange(n, denoms):
    dp = [0]*(n+1)
    dp[0]=1
    denoms.sort()
    for denom in denoms:
        for amount in range(len(dp)):
            if denom<=amount:
                dp[amount]+=dp[amount-denom]
    return dp[-1]



#bottom up
#coin problem
#order important
#example: target amount = 10; coin denominations = [1,5,10,25]. ways= 1coin x 10times, 5coins x 2times,
#(1coin x 5times + 5coin x 1times), 10coin x 1times. But (5coin x 1times + 1coin x 5times) is not an option 
# as (1coin x 5times + 5coin x 1times) is already there.
def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    #pass
    denoms.sort()
    dp = [0]*(n+1)
    dp[-1] = 1
    
    for denom in denoms:
        for amount in reversed(range(len(dp))):
            if denom<=amount:
                #dp[stair]+=dp[stair+jump-1]
                dp[amount-denom]+=dp[amount]

    return dp[0]
