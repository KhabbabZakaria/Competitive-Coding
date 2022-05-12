#given a list with a target number, find the next n bigger values from the target
#use binary tree

x = [0,3,5,1,6,2,4,9,8,7]
x.sort()

L = 0
R = len(x) - 1

target = 5
n = 2

while  L<R-1:
    mid = (L+R)//2
    if x[mid]>=target:
        R = mid
    else:
        L = mid

print(L,R)

print(x[L],x[R])

if x[L] == target:
    index = L
if x[R] == target:
    index = R

print(x[R+1:R+n+1])