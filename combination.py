#from [1,2,3]
#output [[],[1],[2].[3].[1,2],[2,3],[3,1],[1,2,3]]

def powerset(array):
  if len(array)==0:
      return [[]]
  global result
  result = [[], array]
  helper(array, result)
  return result

def helper(array, result):
  if len(array)==0:
    return
  
  for i in range(len(array)):
    popped = array[:].pop(i)
    rest = array[:]
    rest.pop(i)
    if [popped] not in result:
      result.append([popped])
    if rest not in result and len(rest)>1:
      result.append(rest)
    helper(rest, result)
