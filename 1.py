#go through a string and keep removing consecutive same characters if the length of this substring>=3
#Keep doing till there is no such substring left

string = 'caabbbaccacc'

characters = []
count = []
characters.append(string[0])
count.append(1)
for i in range(1, len(string)):
    if count[-1] == 3:
        characters = characters[:-1]
        count = count[:-1]
    try:
        if string[i] != characters[-1]:
            characters.append(string[i])
            count.append(1)
        else:
            count[-1] = count[-1] + 1
    except:
        characters.append(string[i])
        count.append(1)

print(characters)
print(count)

mylist = [a*b for a,b in zip(characters,count)]
print([a*b for a,b in zip(characters,count)])

string = ''.join(str(e) for e in mylist)
print(string)