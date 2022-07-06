def minNumberOfCoinsForChange(n, denoms):
    dp = [float('inf')]*(n+1)
    dp[0] = 0 # min way to make 0 dollars = 0
    for denom in denoms:
        for amount in range(n+1):
            if denom<=amount:
                diff = amount - denom
                dp[amount] = min(dp[amount], 1 + dp[diff])
    if dp[-1]==float('inf'):
        dp[-1] = -1
    return dp[-1]
