###Dấu Ngoặc Hợp Lệ
#Một biểu thức ngoặc là một biểu thức chỉ gồm các loại kí tự ngoặc mở và đóng thuộc ba loại: (), [] hoặc {}. Biểu thức ngoặc được gọi là hợp lệ nếu như nó thỏa mãn các điều kiện sau:

#Số lượng dấu ngoặc đóng và mở của mỗi loại là bằng nhau.
#Liền sau một dấu ngoặc mở bất kỳ luôn luôn phải là một dấu ngoặc mở hoặc đóng cùng loại.
#Ví dụ, các xâu [([)]], {[}] là xâu ngoặc sai quy cách. Còn xâu {[()()][(()())]} là một xâu ngoặc đúng.

#Yêu cầu: Cho trước một xâu ngoặc, hãy kiểm tra xem đó có phải xâu ngoặc đúng hay không?
#

import sys
data = input()
ngoac = []

for i in data:
    ngoac.append(i)
ngoacmo = ["{","[","("]
ngoacdong = ["}","]",")"]
def sovle():
    if(ngoac.count ("(") != ngoac.count(")")):
        return False
    elif(ngoac.count ("{") != ngoac.count("}")):
        return False
    elif(ngoac.count ("[") != ngoac.count("]")):
        return False
    
    for i in range (len(ngoac)):
            if (ngoac[i] == "{"):
                if (ngoac[i+1] not in ngoacmo and ngoac[i+1] != "}"):
                    return False
            if (ngoac[i] == "["):
                if (ngoac[i+1] not in ngoacmo and ngoac[i+1] != "]"):

                    return False
            if (ngoac[i] == "("):
                if (ngoac[i+1] not in ngoacmo and ngoac[i+1] != ")"):

                    return False
    return True
#A = input()


if(sovle() == True):
    print("true")
else: print("fasle")
#print(ngoac)

