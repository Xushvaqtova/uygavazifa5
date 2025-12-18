
# 1-mashq
# Foydalanuvchi ismni kichik harflarda kiritsa, uni bosh harfi katta qilib chiqarish.
'''
a = input("Ismingizni kiriting ")
print(a.title())
'''

# 2-mashq
# Matn kiritilsin, uni capitalize() bilan to‘g‘rilash. Masalan:“python” → “Python”
'''
a = "python"
print(a.capitalize())
'''

# 3-mashq
# “PYTHON” matnini kichik harflarga o‘tkazish.
'''
a = "PYTHON"
print(a.lower())
'''

# 4-mashq
# “SaLoM DuSt” matnini hammasini kichik qilish.
'''
a = "SaLoM DuSt"
print(a.lower())
'''

# 5-mashq
# “Hello” so‘zini 20 uzunlikda markazga joylashtiring.
'''
a = input("So'z yozing ")
print(a.center(20))
'''

# 6-mashq
# “Python” so‘zini 30 uzunlikda “*” belgisi bilan markazga qo‘yish.
'''
a = "Python"
print(a.center(30, "*"))
'''

# 7-mashq
# “banana” so‘zida “a” harfi necha marta qatnashganini toping.
'''
a = "banana"
print(a.count("a"))
'''

# 8-mashq
# “hello world hello” ichida “hello” nechta ekanini sanang.
'''
a = "hello world hello"
print(a.count("hello"))
'''

# 9-mashq  true false qaytaradi
# “hello.txt” fayl nomi .txt bilan tugashini tekshiring.
'''
a = "hello.txt"
print(a.endswith(".txt"))
'''

# 10-mashq
# “picture.png” so‘zi .jpg bilan tugaydimi?
'''
a = "picture.png"
print(a.endswith( ".jpg"))
'''

# 11-mashq
# hello” stringini expandtabs(10) qilib yozing.
'''
a = "H\te\tl\tl\to"
print(a.expandtabs(10))
'''

# 12-mashq
#  “1 2 3” stringini expandtabs(5) qilib chiqaring.
'''
a = "1\t2\t3"
print(a.expandtabs(5))
'''

# 13-mashq
# “hello world” ichida “world” qayerda boshlanishini toping.
'''
a = "hello world"
print(a.find("world"))
'''

# 14-mashq
# “banana” ichida “na” qaysi indexda ekanini toping.
'''
a = input("So'z yozing ")
print(a.index("na"))
'''

# 15-mashq
#  “My name is {}” ichiga “Ali” so‘zini joylashtiring.
'''
a = "Salom mening ismim {ism}"
print(a.format(ism = "Ali"))
'''

# 16-mashq
# “{} + {} = {}” ichiga 3 va 5 sonlarini qo‘yib, natijasini chiqaring.
'''
a = "{} + {} = {}"
print(a.format(3,5, 3+5))
'''

# 17-mashq
# “banana” ichida “na” birinchi qayerda kelishini toping.
'''
a = "banana"
print(a.index("na"))
'''

# 18-mashq
# “python programming” ichida “pro” boshlanish indexini chiqaring.
'''
a = "python programming"
print(a.index("pro"))
'''

# 19-mashq
# “Python3” alfanumerik ekanini tekshiring.
'''
a = "Python3"
print(a.isalnum())
'''

# 20-mashq
# “Hello!” alfanumerik ekanini tekshiring.
'''
a = "Hello!"
print(a.isascii()
'''

# 21-mashq
# “Salom” faqat harflardan tashkil topganmi?
'''
a = "Salom"
print(a.isalpha())
'''

# 22-mashq
# “Salom123” faqat harflardan iboratmi?
'''
a = "Salom123"
print(a.isalpha())
'''

# 23-mashq
# “123” raqamlardan iboratligini tekshiring.
'''
a = "123"
print(a.isnumeric())
'''

# 24-mashq
# “²34” raqammi yoki yo‘qmi (² belgi hisoblanadimi?)
'''
a = "²34"
print(a.isalnum())
'''

# 25-mashq
# “python” faqat kichik harflardan iboratligini tekshiring.
'''
a = "python"
print(a.islower())
'''

# 26-mashq
# “PyThOn” kichik harfmi?
'''
a = "PyThOn"
print(a.islower())
'''

# 27-mashq
# “12345” numeric ekanligini tekshiring.
'''
a = "12345"
print(a.isnumeric())
'''

# 28-mashq
# “⅔” numeric sifatida taniladimi?
'''
a = "⅔"
print(a.isnumeric())
'''

# 29-mashq
# “Hello World!” chop etiladimi?
'''
a = "Hello World!"
print(a.isprintable())
'''

# 30-mashq
# “” chop etiladimi yoki yo‘qmi?
'''
a = ""
print(a.isprintable())
'''

# 31-mashq
#  ” ” (faqat bo‘sh joylar) isspace() natijasini tekshiring.
'''
a = " "
print(a.isspace())
'''

# 32-mashq
# “Hello” isspace() bo‘ladimi?
'''
a = "Hello"
print(a.isspace())
'''

# 33-mashq
# “Hello World” title formatidami?
'''
a = "Hello World"
print(a.istitle())
'''

# 34-mashq
# “hello World” title formatidami?
'''
a = "hello World"
print(a.istitle())
'''

# 35-mashq
# “PYTHON” faqat katta harf ekanligini tekshiring.
'''
a = "PYTHON"
print(a.isupper())
'''

# 36-mashq
# “Python” katta harfmi?
'''
a = "Python"
print(a.isupper())
'''











































