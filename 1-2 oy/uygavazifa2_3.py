# masala 1
'''
def funk1(a, b):
    print(f"Yigindi {a+b}")

funk1(a = int(input("A son kiriting ")), b = int(input("B son kiriting ")))    
'''

# masala 2
'''
def kopfunk(ism, yosh, fam):
    print(f"Ismim {ism}, Familiyam {fam}, yoshim {yosh} da")
    
kopfunk(ism = input("Ismingizni yozing "), fam = input("Familiyangizni yozing "), yosh = int(input("Yoshingizni kiriting ")))    
'''

# masala 3
'''
def funk3(a, b, c):
    return c * (a + b)

print(funk3(2, 3, 4))
     
tomon1 = 6
tomon2 = 10
balandlik = 7

print(funk3(tomon1, tomon2, balandlik))
'''

# masala 4
'''
def argum(*args):
    s = 0
    for i in args:
        s += i
    print(s)    
argum(2, 3, 4, 5, 6)
'''

# masala 5
'''
def argum2(*args):
    print(max(args))
    
argum2(2, 3, 4, 6, 5, )
'''


# masala 5
'''
def maksimal(*args):
    b = 1
    for i in args:
        if b:
            c = i
            b = 0
        else:
            if i > c:
                c = i
    if b:
        print("xato")
    else:
        print(c)

maksimal(3, 6, 1, 9, 11, 23, 4)   
'''

# masala 6
'''
def matn(*args):
    print("Parkda men,", args[0], args[1], args[2], "oynadik.")
    
matn("Lola", "Akmal", "Toxir")
'''


# masala 7
'''
def matn(**kwargs):
    print(f"Ismim {kwargs['ism']}, Familiyam {kwargs['fam']}, yoshim {kwargs['yosh']} da.")

matn(ism = "Ali", fam = "Aliyev", yosh = 17)
'''

# masala 8
'''
def foydalanuvchi(ism, **kwargs):
    print("Ism:", ism)
    for i in kwargs:
        c = kwargs[i]
        print(i,  ":", c)

foydalanuvchi("Ali", yosh = 25, shahar = "Toshkent", kasb = "dasturchi")
'''

# masala 9

# def hisob(*args, **kwargs):
#     if "amal" in kwargs:
#         if kwargs["amal"] == "yigindi":
#             c = 0
#             for i in args:
#                 c +=  i
#             return c
#         elif kwargs["amal"] == "kopaytma":
#             c = 1
#             for i in args:
#                 c *= i
#             return c
#         elif kwargs["amal"] == "ayirma":
#             c = 0
#             for i in args:
#                 c -= i
#             return c
#         elif kwargs["amal"] == "bolinma":
#             c = 1
#             for i in args:
#                 c /= i
#             return c
#         else:
#             return "Amal yoq"
#     else:
#         return "Amal yoq"
#
# print(hisob(1, 2, 3, 4, amal = "yigindi"))
# print(hisob(2, 3, 4, amal = "kopaytma"))
# print(hisob(5, 6, amal = "ayirma"))
# print(hisob(5, 6, amal = "bolinma"))


# masala 10
'''
def malumot(ism, yosh, *args, **kwargs):
    print("Ism:", ism)
    print("Yosh:", yosh)

    for i in args:
        print("Raqam:", i)

    for i in kwargs:
        print(i + ":", kwargs[i])

print("--------")
malumot("Ali", 25, 987651432, manzil = "Toshkent", kasb = "dasturchi")

print("--------")
malumot("Laylo",  21, kasb = "Oqituvchi")
'''


