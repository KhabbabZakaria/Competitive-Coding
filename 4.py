#In bus. passenger in, passenger out
#look before which station the number of passenger is the highest

import heapq

pass_in = [4, 2, 6, 7, 1]
pass_out = [0, 1, 3, 2, 4]


The_Heap = [(i, pass_in[i]) for i in range(len(pass_in))] + [(i, pass_out[i]*(-1)) for i in range(len(pass_out))]

print(The_Heap)
heapq.heapify(The_Heap)
print(The_Heap)

current_pass = 0
max_pass = 0
max_station = None

for i in range(len(The_Heap)):
    station, passenger = heapq.heappop(The_Heap)
    if current_pass > max_pass:
        max_pass = current_pass
        max_station = station

    
print(station, max_pass)
    
