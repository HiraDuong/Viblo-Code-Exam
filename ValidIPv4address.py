# Surely all of us are familiar with the IPV4 addresses - Internet Protocol version 4. An IPV4 address is represented by four 
# 8
# 8-bit integers, separated by ., for example: 192.168.1.1 or 255.255.255.0. Therefore, a string 

# s is an IPV4 address if it meets the following conditions:

# s consists of four integers with values in the range 
# [
# 0
# ,
# 255
# ]
# [0,255].
# Two integers are separated by a .
# Task: Input a string 
# �
# ,
# s, check whether it is a valid IPV4 address.
##############3
def valid_ip(s):
    L = s.split('.')
    if len(L) != 4:
        return False
    A = [eval(i) for i in L]
    for i in A:
        if i <0 or i > 255:
            return False
    return True

s = input()
if valid_ip(s) == True:
    print('Valid')
else :
    print('Invalid')