import math
def tong(x):
    return int(x*(x+1)/2)
def vitri(x):
    return([tong(x-1)+1,tong(x)])

# f = open("input.txt","r")
# data = f.read()
def findx(vt):
    delta = 1+ 8*(vt-1)
    delta2 = 1+8*vt
    return int((1+math.sqrt(delta))/2)

Q = int(input())
for i in range(Q):
    A = [int(j) for j in input().split()]
    x = findx(A[0])
    y = findx(A[1])
    vtx = vitri(x)
    vty = vitri(y)

    result = (vtx[1] - A[0]+1)*x + (A[1]-vty[0]+1)*y 
    for i in range(x+1,y):
        result += i* i
    print(result)