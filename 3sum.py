#all the soring as here the order of the answer was important
#otherwise you don't require the sort()s

def threeNumberSum(array, targetSum):
    # Write your code here.
    #pass
    array.sort()
    final_result = []
    for idx, element in enumerate(array):
        diff = targetSum - element
        result = twosum(array[idx+1:], diff)
        if len(result)>0:
            for j in result:
                j.append(element)
                j.sort()
                final_result.append(j)
    return final_result 
        

def twosum(array, targetSum):
    hashmap = []
    result = []
    for element in array:
        diff = targetSum - element
        if diff not in hashmap:
            hashmap.append(element)
        else:
            result.append([diff, element])
    result.sort()
    return result