def bubbleSort(array):
    # Write your code here.
    #pass
    stop = 0
    while True:
        array, swap_flag = swap(array, stop)
        stop += 1
        if swap_flag==False:
            array, _ = swap(array, stop)
            break
    return array

def swap(temp_array, stop):
    idx = 0
    swap_flag = False
    while idx<len(temp_array)-stop-1:
        if temp_array[idx]>temp_array[idx+1]:
            temp = temp_array[idx+1]
            temp_array[idx+1] = temp_array[idx]
            temp_array[idx] = temp
            swap_flag = True
        idx+=1
    return temp_array, swap_flag
