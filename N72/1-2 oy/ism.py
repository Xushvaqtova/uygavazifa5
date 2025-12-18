# 1-misol
'''
a = int(input("A son kiriting "))
b = int(input("B son kiriting "))
print("Perimetri -", (a + b)*2)
s = a * b
print("Yuzi - ", s)
print("darajasi - ", a ** b)
print("qoldiq - ", a % b)
print("oddiy - ", a / b)
print("2 ta - ", a // b)
'''

#2-misol           MANFIY MUSBAT
'''
a = int(input("Son kiriting "))

if a > 0:
    print("Musbat")
elif a < 0:
    print("Manfiy")
else:
    print("noljon")
'''

#3-misol          JUFT TOQ
'''
a = int(input("Son kiriting "))

if a % 2 == 0:
    print("Juft")
else:
    print("Toq")
'''

# 4-misol        5 VA 7 GA BOLINADIGAN SON
'''
a = int(input("Son kiriting "))

if a % 5 == 0 and a % 7 == 0:
    print("berilgan son 5 va 7ga bolinadi")
elif a % 5 == 0:
    print("faqat 5 ga bolinadi")
elif a % 7 == 0:
    print("faqat 7 ga bolinadi")    
else:
    print("5 va 7 ga bolinmaydi")
'''

#5-misol

a = int(input("Son kiriting "))
if a < 1000 and a > 0:  
    if a >= 400:
        s = a - (a / 2)
        if a == 999:
            print("sizda 50% li skidka bor va siz ", s, "som tolaysiz v bonusiga 100 som olasiz")
        else:
            print("sizda 50% li skidka bor va siz ", s, "som tolaysiz")
    elif a >= 200:
        s = a - (a / 4)
        print("sizda 25% li skidka bor va siz ", s, "som tolaysiz")
    elif a >= 100:
        s = a - (a / 10)
        print("sizda 10% li skidka bor va siz ", s, "som tolaysiz")
    else:
        print("sizda skidka yoq")
        















    
          
