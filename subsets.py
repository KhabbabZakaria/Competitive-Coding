array = [1,2,3]
#answer = [[], [1], [2], [3], [1,2], [2,3], [3,1], [1,2,3]]

def subsets(array, result):
    if len(array)==0:
        if array not in result:
            result.append(array[:])
        return
    
    for i in range(len(array)):
        popped = array.pop(0)
        subsets(array, result)
        array.append(popped)
        array2 = array[:]
        array2.sort()
        if array2 not in result:
            result.append(array2)

result = []
subsets(array, result)

print(result)
