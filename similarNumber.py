step = 0
A = [int(i) for i in input().split()]
n = A[0]
m = A[1]

def FACT(x):
    c2 = 0
    c3 = 0
    while(x % 3 ==0 or x%2 ==0):
        if(x %3 == 0):
            x = x/3
            c3 += 1
        elif(x%2 == 0):
            x = x/2
            c2 +=1
    return[x,c2,c3]

def check(n,m):
    if(m%n !=0):
        return -1
    if(m%3 !=0 and m %2 !=0):
        return -1
    if (m == n):
        return 0
    a = m/n
    res = FACT(a)
    return(res[1] + res[2])

print(check(n,m))
