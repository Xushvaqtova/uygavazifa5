import math


# 1-misol
'''
a = int(input("Son kiriting "))
if a > 0:
    print("Musbat ", a*1)
elif a < 0:
    print("Manfiy ", a)
else:
    print("Nol")
'''

# 2-misol
'''
a = int(input("Son kiriting "))
if a > 0:
    print("Musbat ", a*1)
elif a < 0:
    print("Manfiy ", a-2)
else:
    print("Nol")
'''

# 3-misol
'''
a = int(input("Son kiriting "))
if a > 0:
    print("Musbat ", a*1)
elif a < 0:
    print("Manfiy ", a-2)
else:
    a = 10
    print("Nolga teng ", a )
'''

# 4-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
c = int(input("Son kiriting "))
s = 0
if a > 0:
    s = s + 1
    
if b > 0:
    s = s + 1

if c > 0:
    s = s + 1

print(f"Musbat son {s} ta")
'''

# 5-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
c = int(input("Son kiriting "))
s = 0
d = 0

if a > 0:
    s = s + 1
else:
    d = d + 1
    
if b > 0:
    s = s + 1
else:
    d = d + 1
    
if c > 0:
    s = s + 1
else:
    d = d + 1    

print(f"Musbat son {s} ta")
print(f"Manfiy son {d} ta")
'''

# 6-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
if a > b:
    print("A son katta ", a)
elif a < b:
    print("B son katta ", b)
else:
    print("Ikkkalasi teng ")
'''

# 7-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
if a > b:
    print("B son kichik. Tartib raqami 2", b)
elif a < b:
    print("A son kichik. Tartib raqami 1", a)
else:
    print("Ikkkalasi teng ")
'''


# 8-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
if a > b:
    print(f"A katta {a}, B kichik {b}")
elif a < b:
    print(f"B katta {b}, A kichik {a}")
else:
    print("Ikkkalasi teng ")
'''

# 9-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
c = 0
if a > b:
    c = a
    a = b
    b = c
    print(f"A kichik {a}, B katta {b}")
elif a < b:
    print(f"A kichik {a}, B katta {b}")
else:
    print("Ikkalasi teng")
'''

# 10-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
if a == b:
    s = 0
    print(f"Qiymat {s} ga teng, A - {a}, B - {b}")
else:
    s = a + b
    b = a + b
    print(f"A - {s}, B - {b}")
'''

# 11-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
s = 0
if a == b:
    print(f"Qiymat {s} ga teng, A - {a}, B - {b}")
elif a > b:
    s = s + a
    print(f"A katta {s}")
else:
    s = s + b
    print(f"B katta {s}")
'''          


# 12-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
c = int(input("Son kiriting "))

if a < b and b < c:
    print(f"A son kichik {a}")
elif a > b and b < c:
    print(f"B son kichik {b}")
elif a > b and b > c:
    print(f"C son kichik {c}")
else:
    print("teng")
'''

# 13-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
c = int(input("Son kiriting "))

if a > b and a < c or a < b and a > c:
    print(f"A son orta {a}")
    
elif c > b and a < b or a > b and c < b:
    print(f"B son orta {b}")
    
elif b > c and a < c or a > c and c < b:
    print(f"C son orta {c}")
else:
    print("teng")
'''


# 14-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
c = int(input("Son kiriting "))

if a < b and a < c and c < b:
    print(f"A son kichik - {a}, B son katta - {b}")
elif a < b and a < c and b < c:
    print(f"A son kichik - {a}, C son katta - {c}")

if a > b and b < c and c < a:
    print(f"B son kichik - {b}, A son katta - {a}")
elif a > b and b < c and a < c:
    print(f"B son kichik - {b}, C son katta - {c}")

if a > c and b > c and b < a:
    print(f"C son kichik - {c}, A son katta - {a}")
elif a > c and b > c and a < b:
    print(f"C son kichik - {c}, B son katta - {b}")
else:
    print("qaysidir bir xil raqam")
'''


# 15-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
c = int(input("Son kiriting "))
ab = a + b
ac = a + c
bc = b + c

if ab > ac and ab > bc:
    print(f"A va B sonlar katta. A - {a}, B - {b}")
elif ab < ac and bc < ac:
    print(f"A va C sonlar katta. A - {a}, C - {c}")
if ab < bc and ac < bc:
    print(f" B va C sonlar katta. B - {b}, C - {c}")
else:
    print("Nimadir xato")
'''


# 16-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
c = int(input("Son kiriting "))
if a < b and b < c:
    a = a * 2
    b = b * 2
    c = c * 2
else:
    a = a * (-1)
    b = b * (-1)
    c = c * (-1)
print("A =", a, "B =", b, "C =", c)
'''


# 17-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
c = int(input("Son kiriting "))
if a < b and b < c or a > b and b > c:
    a = a * 2
    b = b * 2
    c = c * 2
else:
    a = a * (-1)
    b = b * (-1)
    c = c * (-1)
print("A =", a, "B =", b, "C =", c)
'''

# 18-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
c = int(input("Son kiriting "))
if a == b and a != c:
    print(f"A va B son teng. C son tengmas. A  - {a}, B - {b}")
elif a == c and a != b:
    print(f"A va C son teng. B son tengmas. A  - {a}, C - {c}")
elif b == c and a != c:
    print(f"C va B son teng. A son tengmas. C  - {c}, B - {b}")
else:
    print("Xatoo")
'''

# 19-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
c = int(input("Son kiriting "))
d = int(input("Son kiriting "))
if a == b and b == c and a != d and b != d and c != d:
    print(f"A, B, C teng D teng emas. A - {a}, B - {b}, C - {c}")
elif a == b and b == d and a != c and b != c and d != c:
    print(f"A, B, D teng C teng emas. A - {a}, B - {b}, D - {d}")
elif a == c and c == d and a != b and c != b and d != b:
    print(f"A, C, D teng B teng emas. A - {a}, C - {c}, D - {d}")
elif b == c and c == d and b != a and c != a and d != a:
    print(f"B, C, D teng A teng emas. B - {b}, C - {c}, D - {d}")
else:
    print("xatooo")
'''

# 20-misol
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
c = int(input("Son kiriting "))
ab = abs(b - a)
ac = abs(c - a)
if ab > ac:
    print(f"C raqam yaqin - {ac}")
elif ab < ac:
    print(f"B raqam yaqin - {ab}")
else:
    print("B va C raqam bir xil ")
'''    

# qoshimcha 1
'''
a = int(input("Son kiriting "))
if 0 >= a:
    print("Sovuq")
elif 20 >= a:
    print("Salqin")
elif 35 >= a:
    print("Iliq")
elif 36 >= a:
    print("Issiq")
'''


# qoshimcha 2
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
c = int(input("Son kiriting "))
if a < b and b < c:
    print("O'sish taribda")
elif a > b and b > c:
    print("Kamayish tartibda")
else:
    print("xato")
'''

# qoshimcha 3
'''
pul = int(input("Pul miqdorini kiriting: "))
if pul >= 10000000:
    pul = pul + pul / 100 * 20 
else:
    pul = pul + pul / 100 * 15
print("Yakuniy summa ", pul)
'''


# qoshimcha 4
'''
a = input("Bugun qanday kun ")  
if a == "yakshanba" or a == "Yakshanba":
    print("Dam olish kuningiz muborak")
else:
    print("Ish kuni")
'''

# qoshimcha 5
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
c = int(input("Son kiriting "))
ab = a + b
ac = a + c
bc = b + c
if ab > ac and ab > bc:
    print("A va B katta", a, b)
elif ac > ab and ac > bc:
    print("A va C katta", a, c)
elif bc > ac and bc > ab:
    print("B va C katta", b, c)    
else:
    print("xato")
'''

# qoshimcha 6
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
if a % 2 != 0 or b % 2 != 0:
    c = a
    a = b
    b = c
print(a, b)
'''

# qoshimcha 7
'''
a = int(input("Son kiriting "))
b = int(input("Son kiriting "))
c = input("Amal kiriting ")
if c == "+":
    d = a + b
elif c == "-":
    d = a - b
elif c == "*":
    d = a * b
elif c == "/":
    d = a / b
else:
    print("Xato amal kiritdingiz")
print(d)    
'''
    
# qoshimcha 8
'''
a = int(input("Son kiriting "))
if a == 12:
    print("Qish fasli")
elif a == 1:
     print("Qish fasli")
elif a == 2:
     print("Qish fasli")     
elif a == 3:
     print("Bahor fasli")
elif a == 4:
     print("Bahor fasli")
elif a == 5:
     print("Bahor fasli")
elif a == 6:
     print("Yoz fasli")
elif a == 7:
     print("Yoz fasli")
elif a == 8:
     print("Yoz fasli")
elif a == 9:
     print("Kuz fasli")
elif a == 10:
     print("Kuz fasli")
elif a == 11:
     print("Kuz fasli")
else:
    print("Xato raqam kiritdingiz")
'''



























