import math

# qoshimcha 1    IF 21
'''
a = int(input("A son kiriting "))
b = int(input("B son kiriting "))
x = 5
y = 6

if a == 0 and b == 0:
    print(0)
elif x == a:
    print(1)
elif y == b:
    print(2)
else:
    print(3)
'''


# qoshimcha 1    IF 22
'''
a = int(input("5  va 6 dn katta son kiriting "))
x = 5
y = 6

if x <= a or y >= a:
    print(a/4)
else:
    print("Kiritgan raaqamingiz OX va OY kordinatalarida bor")
'''


x = int(input("X son kiriting "))
f = 0
if x > 0:
    f = 2 * math.sin(x)
if x <= 0:
    f = x - 6
print(f)    
    
































