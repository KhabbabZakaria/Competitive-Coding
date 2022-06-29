def onerow(prevrow):
    result = [1]
    idx=0
    while idx<len(prevrow)-1:
        result.append(prevrow[idx]+prevrow[idx+1])
        idx+=1
    result.append(1)
    return result

def pascal(N):
    result = [[1], [1,1]]
    n = 3
    return pascalHelper(N, result, n)

def pascalHelper(N, result, n):
    if n>N:
        return result
    else:
        result.append(onerow(result[-1]))
        n+=1
        return pascalHelper(N,result,n)
