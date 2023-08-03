s = input()
A = [int(i) for i in input().split()]
a = A[0] - 1
b = A[1]
new = s[0:a] + s[b:]
print(new)