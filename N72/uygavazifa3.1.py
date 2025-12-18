import sqlite3

#  class 1

# class Car:
#     def __init__(self, name, model, year, price):
#         self.name = name
#         self.model = model
#         self.year= year
#         self.price = price
#
#     def get_name_model(self):
#         return f"\nMashinaning malumotlari\n Nomi: {self.name}\n Modeli: {self.model}\n"
#
#     def get_year_price(self):
#         return f"\nMashinaning malumotlari\n Nomi: {self.year}\n Modeli: {self.price}\n"

#     def get_info(self):
#         return f"\nMashinaning malumotlari\n Nomi: {self.name}\n Modeli: {self.model}\n Yili: {self.year}\n Narxi: {self.price}\n"
#
# m1 = Car('BMW', "M5", 2024, 210000)
# m2 = Car('Audi', "f90", 2020, 27000)
# m3 = Car('Ferrari', "gendle", 2023, 23000)
#
# print(m1.get_name_model())
# print(m2.get_year_price())
# print(m3.get_info())


#  class 2

# class Book:
#     def __init__(self, name, author, type, price):
#         self.name = name
#         self.author = author
#         self.type = type
#         self.price = price
#
#     def get_name_aut(self):
#         return f"\nKitobning malumotlari\n Nomi: {self.name}\n Aftori: {self.author}\n"
#
#     def get_type_price(self):
#         return f"\nKitobning malumotlari\n Turi: {self.type}\n Modeli: {self.price}\n"
#
#     def get_info(self):
#         return f"\nKitobning malumotlari\n Nomi: {self.name}\n Aftori: {self.author}\n Turi: {self.type}\n Narxi: {self.price}\n"
#
# b1 = Book('Mominlarning onalari', "Tavakkal Kenjayev", "Diniy", 50000)
# b2 = Book("Alkimyogar", "Paulo Coelho", "Roman", 50000)
# b3 = Book("O'tkan kunlar", "Abdulla Qodiriy", "Klassika", 45000)
#
# print(b1.get_name_aut())
# print(b2.get_type_price())
# print(b3.get_info())



#  class 3

# class Tree:
#     def __init__(self, name,year, type, price):
#         self.name = name
#         self.year = year
#         self.type = type
#         self.price = price
#
#     def get_name_year(self):
#         return f"\nDaraxt malumotlari\n Nomi: {self.name}\n Yoshi: {self.year}\n"
#
#     def get_type_price(self):
#         return f"\nDaraxt malumotlari\n Turi: {self.type}\n Modeli: {self.price}\n"
#
#     def get_info(self):
#         return f"\nDaraxt malumotlari\n Nomi: {self.name}\n Yoshi: {self.year}\n Turi: {self.type}\n Narxi: {self.price}\n"
#
# t1 = Tree("Olma daraxti", 2010, "Mevali", 150000)
# t2 = Tree("Terak daraxti", 2015, "Manzarali", 100000)
# t3 = Tree("O'rik daraxti", 2012, "Mevali", 120000)
#
# print(t1.get_name_year())
# print(t2.get_type_price())
# print(t3.get_info())


#  class 4

# class Student:
#     def __init__(self, name,age, course, idnum, prof = 'Developer'):
#         self.name = name
#         self.age = age
#         self.curs = course
#         self.id = idnum
#         self.prof = prof
#
#     def get_name_age(self):
#         return f"\nTalaba malumotlari\n Nomi: {self.name}\n Yoshi: {self.age}\n"
#
#     def get_curs_id(self):
#         return f"\nTalaba malumotlari\n Kursi: {self.curs}\n Id raqami: {self.id}\n"
#
#     def get_info(self):
#         return f"\nTalaba malumotlari\n Nomi: {self.name}\n Yoshi: {self.age}\n Kursi: {self.curs}\n Id raqami: {self.id}\n Kasbi: {self.prof}"
#
# s1 = Student("Ali", 20, "Computer Science", 10101, "Shifokor")
# s2 = Student("Malika", 21, "Mathematics", 10203, "Oqituvchi")
# s3 = Student("Javohir", 19, "Physics", 10503, )
#
# print(s1.get_name_age())
# print(s2.get_curs_id())
# print(s3.get_info())


#  class 5

# class Phone:
#     def __init__(self, name, model, komp, year, price, yom):
#         self.name = name
#         self.model = model
#         self.komp = komp
#         self.year = year
#         self.price = price
#         self.yom = yom
#         self.komp = komp
#
#     def get_name_model_komp(self):
#         return f"\nTelefon malumotlari\n Nomi: {self.name}\n Modeli: {self.model}\n Kampaniya: {self.komp}"
#
#     def get_year_price_yom(self):
#         return f"\nTelefon malumotlari\n Yili: {self.year}\n Narxi: {self.price}\n Yomkasti: {self.yom}"
#
#     def get_info(self):
#         return f"\nTelefon malumotlari\n Nomi: {self.name}\n Modeli: {self.model}\n Kampaniya: {self.komp}\n Yili: {self.year}\n Narxi: {self.price}\n Yomkasti: {self.yom}"
#
# p1 = Phone("iPhone", "17 Air", "Apple", 2021, "1200$", 99)
# p2 = Phone("Galaxy", "S23", "Samsung", 2023, "1000$", 98)
# p3 = Phone("Redmi", "Note 12", "Xiaomi", 2022, "350$", 97)
#
# print(p1.get_name_model_komp())
# print(p2.get_year_price_yom())
# print(p3.get_info())


#  Masala 1

# n = "klm"

# if len(n) > 5:
#     s = n[-5:]
# elif len(n) < 5:
#     s = '.' * (5 - len(n)) + n
# else:
#     s = n
# print(s)


#  Masala 2

# n1 = 2
# n2 = 3
# s1 = "assalomu"
# s2 = 'alaykum'
#
# s = s1[:n1]
# d = s2[-n2:]
# sd = s+d
# print(sd)


#  Masala 3

# c = "c"
# s = "cadilac"
# d = ""
# for i in s:
#     if i == c:
#         d += 'c' * 2
#     else:
#         d += i
# print(d)


#  Masala 4

# c = 'c'
# s1 = 'codilac'
# s2 = 'sen'
# d = ""
# for i in s1:
#     if i == c:
#         d += s2 * 1 + c
#     else:
#         d += i
# print(d)


#  Masala 5

# c = 'c'
# s1 = 'codilac'
# s2 = 'sen'
# d = ""
# for i in s1:
#     if i == c:
#         d += c + 1 * s2
#     else:
#         d += i
# print(d)


#  Masala 6

# s1 = 'codilacsen'
# s2 = 'sen'
# if s2 in s1:
#     print(True)
# else:
#     print(False)


#  Masala 7

# s1 = 'sen nima uchun seni sen qildi'
# s2 = 'sen'
# d = s1.count(s2)
# print(d)


#  Masala 8


# s1 = 'sen nima uchun seni sen qildi'
# s2 = 'sen'
# d = s1.replace(s2, '', 1)
# print(d)


#  Masala 9

# s1 = "sen nima uchun seni sen qildi"
# s2 = "sen"
# sozlar = s1.split()
#
# for i in reversed(range(len(sozlar))):
#     if sozlar[i] == s2:
#         sozlar.pop(i)
#         break
# d = " ".join(sozlar)
# print(d)


#  Masala 10

# s1 = "sen nima uchun sening sen qildi"
# s2 = "sen"
# sozlar = s1.split()
#
# for i in reversed(range(len(sozlar))):
#     if sozlar[i] == s2:
#         d = sozlar.pop(i)
# d = " ".join(sozlar)
# print(d)

#  Masala 10                     # 10-misolni ikki xil usulda ishladi qaysi biri togriligini bilmadim

# s1 = "sen nima uchun sening sen qildi"
# s2 = "sen"
# d = s1.replace(s2, '')
# print(d)


#  Masala 11

# s1 = "sen nima uchun sening sen qildi"
# s2 = "sen"
# s3 = "salom dunyo"
#
# d = s1.replace(s2, s3, 1)
# print(d)


 # Masala 12

# s1 = "sen nima uchun seni sen qildi"
# s2 = "sen"
# s3 = "salom"
# sozlar = s1.split()
#
# for i in reversed(range(len(sozlar))):
#     if sozlar[i] == s2:
#         sozlar[i] = s3
#         break
# d = " ".join(sozlar)
# print(d)


#  Masala 13

# s1 = "sen nima uchun sening sen qildi"
# s2 = "sen"
# s3 = "salom"
# d = s1.replace(s2, s3)
# print(d)


# Masala 14

# s1 = "sen nima uchun sening sen qildi"
# f = s1.find(' ')
# s = s1.find(' ', f+1)
# if s == -1:
#     d = ""
# else:
#     d = s1[f+1:s]
# print(d)


# Masala 15

# s1 = "sen nima uchun sening sen qildi"
# f = s1.find(' ')
# s = s1.rfind(' ')
# if f == s:
#     d = ""
# else:
#     d = s1[f+1:s]
# print(d)

