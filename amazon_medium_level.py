#given an integer array nums and an integer k, return the k most frequent elements. order not important
#constraint len(nums) \in [10**5]
import heapq

def fn(nums, k):
    thelist = []
    numlist = []
    frequncy = []
    for i in range(len(nums)):
        if nums[i] in numlist:
            ind = numlist.index(nums[i])
            old_element = (frequncy[ind], numlist[ind])
            index = thelist.index(old_element)
            thelist.pop(index)
            frequncy[ind] = frequncy[ind] - 1
            thelist.append((frequncy[ind], nums[i]))
        else:
            thelist.append((-1, nums[i]))
            numlist.append(nums[i])
            frequncy.append(-1)
    

    heapq.heapify(thelist)
    for i in range(k):
        _, number = heapq.heappop(thelist)
        print(number)

    

nums = [1,1,1,2,2,3]
k = 2
fn(nums,k)