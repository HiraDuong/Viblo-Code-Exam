# KAPREKAR

# Written by Vu Huy Hoang (火楽皆本)

import math

def split_no_space(string):
    A= []
    for i in string:
        A.append(i)
    return A

def KAPREKAR_check(n):
    
    n_string = str(n)
    arr = split_no_space(n_string)
    arr.sort()
    max_str = ""
    min_str = ""
    for i in arr:
        min_str+=i
    arr.sort(reverse= True)
    for i in arr: 
        max_str+=i
    
    x = int(max_str)
    y = int(min_str)
    if (x-y == n):
        return n
    else : return KAPREKAR_check(x-y)


n = int(input())
m = KAPREKAR_check(n)

if ( n > m) : 
    a = n
    while(n>m):
        m = KAPREKAR_check(2*a)
        a *=2
    print(m)

else : 
    print(m)