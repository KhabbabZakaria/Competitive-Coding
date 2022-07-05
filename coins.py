array = [7,5,1]
target = 18

result = []
mincount = float('inf')
count = 1
def coins(array, target, count):
    global mincount
    if target ==0:
        return 
    for i in array:
        diff = target - i
        if diff>=0:
            count+=1
            coins(array, diff, count)
    if count<mincount:
        mincount=count
    count=1

coins(array, target, count)
print(mincount)
