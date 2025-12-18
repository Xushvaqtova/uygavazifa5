import math

# 1-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
for i in range(a):
    print(b) 
'''

# 2-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
s = 0
for i in range(a, b+1):
    print(i)
    s += 1
print(f"{s} ta raqam bor")    
'''

# 3-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
s = 0
for i in range(a-1, b, -1):
    print(i)
    s += 1
print(f"{s} ta raqam bor")  
'''

# 4-misol
'''
a = int(input("Konfet narxini kiriting "))
for i in range(1, 10):
    print(f"{i} kg konfetning narxi ", i*a, " som turadi")
'''

# 5-misol
'''
n = float(input("1 kg konfet narxini kiriting: "))
for i in range(1, 11):
    kg = i / 10
    summa = n * kg
    print(f"{kg} gramm konfetning narxi = {summa}")
'''

# 7-misol
'''
a = int(input("A sonni kiriting "))
b = int(input("B sonni kiriting "))
d = 0
for i in range(a, b+1):
    yigindi += i
print(f"{a} dan {b} gacha bolgan sonlar yigindisi = {d}")
'''

# 8-misol
'''
a = int(input("A sonni kiriting "))
b = int(input("B sonni kiriting "))
d = 1
for i in range(a, b+1):
    d *= i
print(f"{a} dan {b} gacha bolgan sonlar kopaytmasi = {d}")
'''

# 9-misol
'''
a = int(input("A sonni kiriting "))
b = int(input("B sonni kiriting "))
d = 0
for i in range(a, b+1):
    d += i**2
print(f"{a} dan {b} gacha bolgan sonlar kvadratlari yigindisi = {d}")
'''

# 10-misol
'''
a = int(input("A sonni kiriting "))
b = 0
for i in range(1, a+1):
    b += i + 1
    print(f"{i} aylanish B = {b} ga teng")

print("Barcha sonlar yigindisi ", b)
'''

# 11-misol
'''
a = int(input("A sonni kiriting "))
s = 0
for i in range(1, a+1):
    s += (i+1)**2
    print(f"{i} aylanish S = {s} ga teng")
print("Barcha sonlar yigindisi ", s)
'''

# 12-misol
'''
n = float(input("A sonni kiriting "))
s = 1.0
for i in range(1, int(n) + 1):  
    b = 1 + i / 10.0
    s *= b
print("Barcha sonlar yigindisi ", s)
'''

# 14-misol

'''
a = int(input("A sonni kiriting "))
s = 0
for i in range(1, a+1):
    b = 2*i - 1
    s += b
    print(f"Qadam {i}: kvadrat = {s}")
'''

# 15-misol
'''
a = float(input("A sonni kiriting "))
d = int(input("Darajani kiriting "))
s = 1
for i in range(d):
    s *= a
print(f"{a} ning {d}-darajasi = {s}")
'''

# 16-misol
'''
a = float(input("A sonni kiriting "))
d = int(input("Daraja kiriting "))
s = 1
for i in range(1, d+1):
    s *= a
    print(f"{a} ning {i}-darajasi = {s}")
'''

# 17-misol
'''
a = float(input("A sonni kiriting "))
d = int(input("Daraja kiriting "))
s = 0
b = 1
for i in range(1, d + 1):
    b *= a
    s += b
print("Yig'indi:", s)
'''

# 19-misol
'''
a = ft(input("A sonni kiriting "))
b = 1
for i in range(1, n + 1):
    b *= i
print(f"{n} =", b)
'''

# 20-misol
'''
a = int(input("A sonni kiriting "))
b = 0
for i in range(0, a + 1):
    b += i
print(f"{a} =", b)
'''


# Qoshimcha 1
'''
a = int(input("A ni kiriting: "))
b = int(input("B ni kiriting: "))

for i in range(a, b+1):
    if i % 2 == 0:
        print(i)
'''


# Qoshimcha 2
'''
a = int(input("Son kiriting "))

for i in range(2, a+1):
    s = 0
    for j in range(1, i):
        if i % j == 0:
            s += j
    if s == i:
        print(i)

'''

# Qoshimcha 3
'''
a = int(input("A sonni kiriting "))
b = int(input("B sonni kiriting "))
for i in range(1, min(a, b) + 1): # min() ni w3schooldan topdim
    if a % i == 0 and b % i == 0:
        print(i)
'''

# Qoshimcha 4

a = int(input("A son kiriting "))
b = int(input("B son kiriting "))
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        e = i
print(i)

# Qoshimcha 6
'''
n = int(input("Son kiriting "))

for i in range(1, n + 1):
    bir = i % 10
    ikki = i // 10
    kopaytma = ikki * bir

    if kopaytma > 10:
        print(i) 
'''      

'''
a = int(input("Son kiriting "))

for i in range(1, a + 1):
    s = i ** 2
    if s % 2 == 1:
        print(s)

'''


'''
a = int(input("Oy raqam kiriting "))
b = int(input("Kun raqam kiriting "))

if b > 0 and b < 32:
    if a == 1 and b < 32:
        print(f"{b}-Yanvar")
    elif a == 2 and b < 29:
            print(f"{b}-Fevral")
        else:
            print("Fevralda unday kun yoq")
    elif a == 3 and b < 31:
        print(f"{b}-Mart")
    elif a == 4 and b < 32:
        print(f"{b}-Aprel")    
    elif a == 5 and b < 31:
        print(f"{b}-May")
    elif a == 6 and b < 32:
        print(f"{b}-Iyun")
    elif a == 7 and b < 31:
        print(f"{b}-Iyul")
    elif a == 8 and b < 32:
        print(f"{b}-Avgust")
    elif a == 9 and b < 31:
        print(f"{b}-Sentabr")
    elif a == 10 and b < 32:
        print(f"{b}-Oktabr")
    elif a == 11 and b < 31:
        print(f"{b}-Noyabr")
    elif a == 12 and b < 32:
        print(f"{b}-Dekabr")    
    else:
        print("Xato oy kiritdingiz!")
else:
    print("xato kun kiritdingiz")
'''


'''
a = int(input("Raqam kiriting "))

for i in range(1, a+1):
    for j in range(1, 10+1):
        print(f"{i} x {j} = {a*j}")
    print("---------------------------------")    
'''    

'''
a = int(input("Son kiriting "))
for i in range(1, a + 1):
    s = i ** 2
    if s < 50 :
        print(s)
'''

'''
a = int(input("Son kiriting "))
if a % 2 == 0:
    print(a-1)
else:
    print(a-2)
'''

a = int(input("Son kiriting "))
for i in range(1, a+1):
    s  = 0
    for j in range(1, i+1):
        if i % j == 0:
            s += 1

    if s == 2:
        print(i)







    
