
def find_max_mul(A):
    B = []
    mul = 1
    count = 0
    for i in A:
        if i < 0: 
            count+=1
            B.append(i)
        if i == 0:
            A.remove(i)
    if count % 2 == 0:
        for i in A :
            mul *= i
        return mul
    else:
        k = max(B)
        A.remove(k)
        for i in A :
            mul *= i
        return mul 

        

An = [int (i) for i in (input().split()) ]
Binh = [int (i) for i in (input().split()) ]

x = find_max_mul(An)
y = find_max_mul(Binh)

if (x > y): 
    print("An")
elif (x == y):
    print("Draw")
else : 
    print("Binh")