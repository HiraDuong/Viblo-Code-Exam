
# a^b mod n
# tính lũy thừa nhanh
def Mod_Exponentiation(a,b,n):
	if b == 0:
		return 1
	if b == 1:
		return a
	r = Mod_Exponentiation(a, b//2, n)
	r = (r*r)%n
	if b % 2 == 1:
		r = (r*a)%n
	return r%n
A = [int(i) for i in input().split()]
c = pow(10,9) +7
#print(c)
print(Mod_Exponentiation(A[0],A[1],c))