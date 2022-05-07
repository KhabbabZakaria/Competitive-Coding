#2 Sum problem
#using hashmaps

thelist = [2,1,5,3,8]
target = 5

number = []
index = []

def fn():
    for i in range(len(thelist)):
        sub = target - thelist[i]
        if sub not in number:
            number.append(thelist[i])
            index.append(i)
        else:
            return (number.index(sub), i)


print(fn())


