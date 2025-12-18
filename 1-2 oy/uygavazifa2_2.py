# 1-masala
'''
a = int(input("A son kiriting "))
b = int(input("B son kiriting "))
while a > b:
    a = a-b
print(a)
'''

# 2-masala
'''
a = int(input("A son kiriting "))
b = int(input("B son kiriting "))
s = 0
while a > b:
    a = a-b
    s += 1
print(s)
'''

# 3-masala
'''
a = int(input("A son kiriting "))
b = int(input("B son kiriting "))
s = 0
while a > b:
    a = a-b
    s += 1
print(f"Qoldiq - {a}")
print(f"Butun - {s}")
'''

# 4-masala
'''
n = int(input("A son kiriting "))
d = 1
while n > d:
    d *= 3
if d == n:
    print("Daraja")
else:
    print("Daraja emas")
'''

# 5-masala
'''
a = int(input("A son kiriting "))
s = 0
d = 1
while a > d:
    d *= 2
    s += 1

if d == a:
    print("Daraja")
else:
    print("Daraja emas")
'''

# 6-masala
'''
a = int(input("A son kiriting "))
s = 0
d = 1
while a > s:
    d  = d *(a-s)
    s += 2
print(d)
'''

# 7-masala
'''
a = int(input("A son kiriting "))
d = 1
while a > d**2:
    d += 1 
print(d)
'''


# 8-masala
'''
a = int(input("A son kiriting "))
d = 1
while a >= (d+1)*(d+1):
    d += 1 
print(d)
'''

# 1-masala
'''
a = int(input("A son kiriting "))
while a > 0:
    if "7" in str(a):
        print(a)
    a -= 1 
'''

# 2-masala
'''
n = int(input("Sonni kiriting "))
i = 2
tub = True
while i < n:
    if n % i == 0:
        tub = False
    i += 1
    
if tub and n > 1:
    print("Tub")
else:
    print("Murakkab")
'''

# 3-masala
'''
n = int(input("n ni kiriting "))
i = 2

while i <= n:
    j = 2
    tub = True
    while j < i:
        if i % j == 0:
            tub = False
        j += 1
    if tub:
        print(i)
    i += 1
'''

# 4-masala
'''
x = int(input("Oylagan son kiriting "))
komp = 1
urinish = 0

while komp != x:
    komp += 1
    urinish += 1
urinish += 1   
print(f"kompyuter {urinish} marta topdi")
'''


# 5-masala
'''
a = int(input("Son kiriting "))
b = int(input("Orni "))
i = 1
raqam = 0
while i <= b:
    raqam = a % 10
    a = a // 10
    i += 1
print(raqam)
'''


# Qoshimcha 1
'''
a = int(input("A son kiriting "))
b = int(input("B son kiriting "))
while a <= b:
    print(a)
    a += 1
'''

# Qoshimcha 2
'''
a = int(input("A son kiriting "))
b = int(input("B son kiriting "))
s = 1
while a <= b:
    s = a ** 2
    print(s)
    a += 1
'''

# Qoshimcha 3
'''
a = int(input("A son kiriting "))
b = int(input("B son kiriting "))
while a <= b:
    if a % 7 == 0:
        print(a)
    a += 1
'''

# Qoshimcha 4
'''
a = int(input("A son kiriting "))
while 1 <= a:
    if a % 3 == 0:
        print(a)
    a -= 1
'''

# Qoshimcha 5
'''
n = int(input("Son kiriting "))
s = 0
while n > 0:
    n = n // 10   
    s += 1
print(s, "xonali son")
'''


# Qoshimcha 6
'''
n = int(input("Son kiriting "))
s = n
while n > 0:
    n = int(input("Son kiriting "))
    s += n
print(s)
'''

# Qoshimcha 9
'''
n = int(input("Son kiriting "))
s = 1
d = 1
while n >= s:
    d *=  s
    s += 1
print(d)
'''    

# Qoshimcha 10
'''
s = 1  
while s != 0:
    s = int(input("Son kiriting "))
    if s > 0:
        print(s ** 2)
'''
















