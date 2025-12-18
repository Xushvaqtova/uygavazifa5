# class 1

# class Talaba:
#     def __init__(self, name, age, id, curs):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.curs = curs
#
#     def get_info(self):
#         return f" Ism: {self.name}\n Yosh: {self.age}\n Id: {self.id}\n Kurs: {self.curs}\n"
#
# class Center:
#     def __init__(self, nomi, manzil):
#         self.nomi = nomi
#         self.manzil = manzil
#         self.talaba_soni = 0
#         self.talabalar = []
#
#     def add_talabalar(self, talaba):
#         self.talaba_soni += 1
#         self.talabalar.append(talaba)
#
#     def get_talabalar(self):
#         for i in self.talabalar:
#             print(i.get_info())
#
# t1 = Talaba("Madina", 19, 37641, "Python")
# t2 = Talaba("Ali", 22, 23455, "Java")
# t3 = Talaba("Aslzoda", 23, 245655, "Smm")
#
# c1 = Center("NT", "Chilonzor")
#
# c1.add_talabalar(t1)
# c1.add_talabalar(t2)
# c1.add_talabalar(t3)
#
# c1.get_talabalar()
# print(c1.talaba_soni)

# class 2


# class Car:
#     def __init__(self, name, model, price, color):
#         self.name = name
#         self.model = model
#         self.price = price
#         self.color= color
#
#     def get_info(self):
#         return f" Ism: {self.name}\n Modeli: {self.model}\n Narxi: {self.price}\n Rangi: {self.color}\n"
#
# class Zavod:
#     def __init__(self, nomi, manzil):
#         self.nomi = nomi
#         self.manzil = manzil
#         self.mashina_soni = 0
#         self.mashinalar = []
#
#     def add_mashina(self, car):
#         self.mashina_soni += 1
#         self.mashinalar.append(car)
#
#     def get_mashina(self):
#         for i in self.mashinalar:
#             print(i.get_info())
#
# c1 = Car("BMW", "M5", 3764541, "Kok")
# c2 = Car("AUDI", "X5", 23456455, "Qora")
# c3 = Car("BYD", "Song plus", 24545655, "Qizil")
#
# z1 = Zavod("Yasmina", "Yashnabod")
#
# z1.add_mashina(c1)
# z1.add_mashina(c2)
# z1.add_mashina(c3)
#
# z1.get_mashina()


# class 3

# class Teacher:
#     def __init__(self, name, age, specil, price):
#         self.name = name
#         self.age = age
#         self.specil = specil
#         self.price = price
#
#     def get_info(self):
#         return f" Ism: {self.name}\n Yosh: {self.age}\n Mutaxassisligi: {self.specil}\n Oyligi: {self.price}\n"
#
# class Center:
#     def __init__(self, nomi, manzil):
#         self.nomi = nomi
#         self.manzil = manzil
#         self.tech_soni = 0
#         self.teachers = []
#
#     def add_teachers(self, tech):
#         self.tech_soni += 1
#         self.teachers.append(tech)
#
#     def get_teachers(self):
#         for i in self.teachers:
#             print(i.get_info())
#
# t1 = Teacher("Madina", 22,  "Python", 12000000)
# t2 = Teacher("Ali", 25, "Java", 15000000)
# t3 = Teacher("Aslzoda", 28, "Smm", 18000000)
#
# c1 = Center("NT", "Fargona filiali")
#
# c1.add_teachers(t1)
# c1.add_teachers(t2)
# c1.add_teachers(t3)
#
# c1.get_teachers()


# class 4

# class Suv:
#     def __init__(self, name, price, length):
#         self.name = name
#         self.price = price
#         self.length = length
#
#     def get_info(self):
#         return f" Ism: {self.name}\n Narxi: {self.price}\n Qanchaligi: {self.length}\n"
#
# class Dokon:
#     def __init__(self, nomi, manzil):
#         self.nomi = nomi
#         self.manzil = manzil
#         self.suv_soni = 0
#         self.suvlar = []
#
#     def add_water(self, suv):
#         self.suv_soni += 1
#         self.suvlar.append(suv)
#
#     def get_water(self):
#         for i in self.suvlar:
#             print(i.get_info())
#
# w1 = Suv("Madina", 9000, "0.5 litr")
# w2 = Suv("Ali", 11000, "1 litr")
# w3 = Suv("Aslzoda", 15000, "1.5 litr")
#
# d1 = Dokon("Zeydil", "Mirobod")
#
# d1.add_water(w1)
# d1.add_water(w2)
# d1.add_water(w3)
#
# d1.get_water()




# Masala 1
from turtledemo.chaos import jumpto

# n = int(input("n = "))
# new = []
# for i in range(n+1):
#     son = i*2+1
#     new.append(son)
# print(new)


# Masala 2

# n = [4, 5, 7, 8, 6, 9]
# new = []
# for i in n:
#     new.append(2**i)
# print(new)


# Masala 3




# Masala 4





# Masala 5

# n = 7
# f = [1, 1]
# for i in range(2, n):
#     new = f[i-1] + f[-2]
#     f.append(new)
# print(f)


# Masala 6

# n = 5
# A = 2
# B = 4
# a = [A, B]
# for i in range(2, n+1):
#     new = a[i-1] + a[i-2]
#     a.append(new)
# print(a)


# Masala 7

# n = [4, 5, 7, 8, 6, 9]
# new = []
# for i in reversed(n):
#     new.append(i)
# print(new)


# Masala 8

# massiv = [4, 5, 7, 8, 6, 9]
# new = []
# for i in massiv:
#     if i % 2 != 0:
#         new.append(i)
# print(f"Natija: {new}, toqlar soni: {len(new)}")


# Masala 9

# massiv = [4, 5, 7, 8, 6, 9]
# new = []
# for i in reversed(massiv):
#     if i % 2 == 0:
#         new.append(i)
# print(f"Natija: {new}, juftlar soni: {len(new)}")


# Masala 10

# massiv = [4, 5, 7, 8, 6, 9]
# juft = []
# toq = []
# for i in massiv:
#     if i % 2 == 0:
#         juft.append(i)
#     else:
#         toq.append(i)
# new = juft + toq[::-1]
# print(new)


# Masala 11

# n = 10
# k = 3
# a = [5, 7, 2, 9, 6, 4, 8, 3, 1, 10]
# new = []
# for i in range(k, n, k):
#     new.append(a[i])
# print(new)


# Masala 12

# n = 8
# a = [4, 7, 9, 2, 6, 1, 5, 8]
# new = []
# for i in range(0, n, 2):
#         new.append(a[i])
# print(new)


# Masala 13

# n = 8
# a = [4, 7, 9, 2, 6, 1, 5, 8]
# new = []
# for i in range(1, n, 2):
#         new.append(a[i])
# print(new)


# Masala 14

# n = 6
# massiv = [4, 5, 7, 8, 6, 9]
# juft = []
# toq = []
# for i in range(0, n, 2):
#     juft.append(massiv[i])
# for i in range(1, n, 2):
#     toq.append(massiv[i])
# new = juft + toq
# print(new)


# Masala 15

# n = 6
# massiv = [4, 5, 7, 8, 6, 9]
# juft = []
# toq = []
# for i in range(0, n, 2):
#     juft.append(massiv[i])
# for i in range(1, n, 2):
#     toq.append(massiv[i])
# new = toq + juft[::-1]
# print(new)


# Masala 16


# n = 6
# massiv = [4, 5, 7, 8, 6, 9]
# new = []
# for i in range(n//2):
#     new.append(massiv[i])
#     new.append(massiv[n-1-i])
# if n % 2 == 1:
#     new.append(massiv[n//2])
# print(new)


# Masala 17



