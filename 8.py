
def fn(list1, list2):
    list3 = list1+list2
    list3.sort()
    if len(list3)%2!=0:
        return list3[len(list3)//2]
    else:
        return (list3[len(list3)//2 - 1] + list3[len(list3)//2])/2


x =fn([1,3], [2])

print(x)