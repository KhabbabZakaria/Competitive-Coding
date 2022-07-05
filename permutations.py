array = [1,2,3]
#answer = [[1,2,3], [2,3,1], [3,2,1], [1,3,2], [2,1,3], [3,1,2]]]


def combination(array):
    length = len(array)
    if length==0:
        return 1
    return length*combination(array[1:])

result = [array[:]]
def permutation(array, result):
    if len(array)==0:
        result.append([array[:]])

    if len(result)==combination(array):
        return
    else:
        for i in range(len(array)):
            popped = array.pop(i)
            array.append(popped)
            if array not in result:
                result.append(array[:])
                permutation(array, result)
            else:
                continue

permutation(array, result)
print(result)
