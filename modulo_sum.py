def solve(n,k):
    a = int(n/k)
    res = a* (k-1)*k/2
    m = a*k
    for i in range (m,n+1):
        res += i%k
    return res
c = pow (10,9)+7

T = int(input())

for j in range(T):
    A = [int(i) for i in input().split()]
    n = A[0]
    k = A[1]
    r = solve(n,k)
    print(int(r%c))
