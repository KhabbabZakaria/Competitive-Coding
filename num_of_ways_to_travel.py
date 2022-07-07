#calculate number of ways to travel from a place to other 
#options = right or down
#example:
# 0 _
# _ _
# _ N
# there are 3 ways from 0 to N = (right,down,down), (down,right,down), (down,down,right)

def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    E = [[0]*(width) for _ in range(height)]
    for w in range(width):
        E[0][w] = 1
    for h in range(height):
        E[h][0] = 1
    for w in range(1,width):
        for h in range(1,height):
            E[h][w] = E[h-1][w] + E[h][w-1]

    return E[-1][-1]
