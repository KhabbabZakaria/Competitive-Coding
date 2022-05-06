#finding neighbors

x = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

neighbor_coordinate = [[1,0], [-1,0], [0,1], [0,-1]]
input_coordinate = [1,1]

neighbors = []

for n in neighbor_coordinate:
    if input_coordinate[0] + n[0]>=0 and input_coordinate[1] + n[1]>=0:
        try:
            neighbors.append(x[input_coordinate[0] + n[0]][input_coordinate[1] + n[1]])
        except:
            pass

print(neighbors)

