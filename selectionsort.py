def selectionSort(array):
    # Write your code here.
    #pass
    start = 0
    while True:
        unsorted_part = array[start:]
        min_idx, _ = find_min(unsorted_part)
        array[start], array[start+min_idx] = array[start+min_idx], array[start]
        start += 1
        if start >= len(array) - 1:
            break
    return array

def find_min(unsorted_part):
    min_idx, min_val = 0, unsorted_part[0]
    for idx in range(1,len(unsorted_part)):
        val = unsorted_part[idx]
        if val < min_val:
            min_idx, min_val = idx, val
    return min_idx, min_val



