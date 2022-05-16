#find longest substring out of a string where the substring wont have duplicates.

import heapq

def fn(string):
    substrings = []
    i = 0
    while i<len(string):
        temp = [string[i]]
        for j in range(i+1, len(string)):
            if string[j] not in temp:
                temp.append(string[j])
            else:
                break
        substring = ''.join(str(e) for e in temp)
        substrings.append((-len(substring), substring))
        i = i+1
    heapq.heapify(substrings)
    length, substring = heapq.heappop(substrings)
    return -length, substring


x = fn('pwwkew')
print(x)