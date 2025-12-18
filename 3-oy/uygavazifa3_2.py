# Class 1

# class Car:
#     def __init__(self, name, model, year, price):
#         self.name = name
#         self.model = model
#         self.year = year
#         self.price = price
#
#     def get_info(self):
#         return f"\n Malumotlar:\n Nomi: {self.name}\n Modeli: {self.model}\n Yili: {self.year}\n Narxi: {self.price}$"
#
# class LuxuryCar(Car):
#     def __init__(self, name, model, year, price, salon, autopilot):
#         super().__init__(name, model, year, price)
#         self.salon = salon
#         self.autopilot = autopilot
#
#     def get_luxury_info(self):
#         return f"\n Luxury mashina malumotlari:\n Nomi: {self.name}\n Modeli: {self.model}\n Yili: {self.year}\n Narxi: {self.price}$\n Salon turi: {self.salon}\n Avtopilot: {self.autopilot}"
#
# class ElectricCar(LuxuryCar):
#     def __init__(self, name, model, year, price, salon, autopilot, battery, charge_time):
#         super().__init__(name, model, year, price, salon, autopilot)
#         self.battery = battery
#         self.charge_time = charge_time
#
#     def get_electric_info(self):
#         return f"\n Elektr malumotlari:\n Nomi: {self.name}\n Modeli: {self.model}\n Yili: {self.year}\n Narxi: {self.price}$\n Salon turi: {self.salon}\n Avtopilot: {self.autopilot}\n Bateriya sig'imi: {self.battery}\n Zaryad vaqti: {self.charge_time} soat"
#
# car1 = Car("BMW", "M5", 2024, 210000)
# lux1 = LuxuryCar("Mercedes", "S-Class", 2023, 150000, "Charm", "Bor")
# elec1 = ElectricCar("Tesla", "Model X", 2025, 120000, "Eko charm", "Bor", 120, 2)
#
# print(car1.get_info())
# print(lux1.get_luxury_info())
# print(elec1.get_electric_info())


# Class 2

# class Book:
#     def __init__(self, name, author, type, price):
#         self.name = name
#         self.author = author
#         self.type = type
#         self.price = price
#
#     def get_info(self):
#         return f"\n Odatiy kitob malumotlari:\n Nomi: {self.name}\n Muallifi: {self.author}\n Turi: {self.type}\n Narxi: {self.price} so'm"
#
# class EBook(Book):
#     def __init__(self, name, author, type, price, file_size, file_format):
#         super().__init__(name, author, type, price)
#         self.file_size = file_size
#         self.file_format = file_format
#
#     def get_ebook_info(self):
#         return f"\n Elektron kitob malumotlari:\n Nomi: {self.name}\n Muallifi: {self.author}\n Turi: {self.type}\n Narxi: {self.price} so'm\n Fayl hajmi: {self.file_size} MB\n Format: {self.file_format}"
#
# class AudioBook(EBook):
#     def __init__(self, name, author, type, price, file_size, file_format, duration, narrator):
#         super().__init__(name, author, type, price, file_size, file_format)
#         self.duration = duration
#         self.narrator = narrator
#
#     def get_audiobook_info(self):
#         return f"\n Audio kitob malumotlari:\n Nomi: {self.name}\n Muallifi: {self.author}\n Turi: {self.type}\n Narxi: {self.price} so'm\n Fayl hajmi: {self.file_size} MB\n Format: {self.file_format}\n Davomiyligi: {self.duration} soat\n Ovoz bergan: {self.narrator}"
#
# b1 = Book("O'tkan kunlar", "Abdulla Qodiriy", "Klassika", 45000)
# b2 = EBook("Alkimyogar", "Paulo Coelho", "Roman", 50000, 2, "PDF")
# b3 = AudioBook("Mominlarning onalari", "Tavakkal Kenjayev", "Diniy", 50000, 5, "MP3", 12, "Islom Abdug‘aniyev")
#
# print(b1.get_info())
# print(b2.get_ebook_info())
# print(b3.get_audiobook_info())


# class 3

# class Book:
#     def __init__(self, name, author, type, price):
#         self.name = name
#         self.author = author
#         self.type = type
#         self.price = price
#
#     def get_info(self):
#         return f"\n Kitob malumotlari:\n Nomi: {self.name}\n Muallifi: {self.author}\n Turi: {self.type}\n Narxi: {self.price} so'm\n"
#
# class Kutubxona:
#     def __init__(self, location, lib_name):
#         self.location = location
#         self.lib_name = lib_name
#
#     def get_lib_info(self):
#         return f"\n Kutubxona malumotlari:\n Nomi: {self.lib_name}\n Joylashuvi: {self.location}\n"
#
# class Oquvchi(Book, Kutubxona):
#     def __init__(self, name, author, type, price, location, lib_name, reader_name):
#         Book.__init__(self, name, author, type, price)
#         Kutubxona.__init__(self, location, lib_name)
#         self.reader_name = reader_name
#
#     def get_reader_info(self):
#         return f"\n Oquvchi: {self.reader_name}\n {self.get_info()} {self.get_lib_info()}"
#
# o1 = Oquvchi("Alkimyogar", "Paulo Coelho", "Roman", 50000, "Toshkent markaziy", "Respublika Kutubxonasi", "Sevinch")
# o2 = Oquvchi("O'tkan kunlar", "Abdulla Qodiriy", "Klassika", 45000, "Samarqand", "Viloyat Kutubxonasi", "Aziz")
#
# print(o1.get_reader_info())
# print(o2.get_reader_info())


# class 4

# class Car:
#     def __init__(self, name, model, year, price):
#         self.name = name
#         self.model = model
#         self.year = year
#         self.price = price
#
#     def get_car_info(self):
#         return f"\n Mashina malumotlari:\n Nomi: {self.name}\n Modeli: {self.model}\n Yili: {self.year}\n Narxi: {self.price} $\n"
#
# class Zavod:
#     def __init__(self, zavod_name, country):
#         self.zavod_name = zavod_name
#         self.country = country
#
#     def get_zavod_info(self):
#         return f"\n Zavod malumotlari:\n Nomi: {self.zavod_name}\n Mamlakat: {self.country}\n"
#
# class Klient(Car, Zavod):
#     def __init__(self, name, model, year, price, zavod_name, country, client_name):
#         Car.__init__(self, name, model, year, price)
#         Zavod.__init__(self, zavod_name, country)
#         self.client_name = client_name
#
#     def get_full_info(self):
#         return f"\n Klient: {self.client_name}\n {self.get_car_info()} {self.get_zavod_info()}"
#
# k1 = Klient("BMW", "M5", 2023, 120000,"BMW AG", "Germaniya", "Sevinch")
# k2 = Klient("Chevrolet", "Cobalt", 2022, 12000,"UzAuto Motors", "O‘zbekiston", "Aziz")
#
# print(k1.get_full_info())
# print(k2.get_full_info())


# class 5

# class House:
#     def __init__(self, rooms, price):
#         self.rooms = rooms
#         self.price = price
#
#     def get_house_info(self):
#         return f"\n Uy malumotlari:\n Xonalar soni: {self.rooms}\n Narxi: {self.price} $\n"
#
# class Location:
#     def __init__(self, city, district):
#         self.city = city
#         self.district = district
#
#     def get_location_info(self):
#         return f"\n Joylashuv:\n Shahar: {self.city}\n Tuman: {self.district}\n"
#
# class Owner(House, Location):
#     def __init__(self, rooms, price, city, district, owner_name):
#         House.__init__(self, rooms, price)
#         Location.__init__(self, city, district)
#         self.owner_name = owner_name
#
#     def get_full_info(self):
#         return f"\n Uy egasi: {self.owner_name}\n {self.get_house_info()} {self.get_location_info()}"
#
# o1 = Owner(5, 120000, "Toshkent", "Mirzo Ulug‘bek", "Sevinch")
# o2 = Owner(3, 60000, "Samarqand", "Urgut", "Aziz")
#
# print(o1.get_full_info())
# print(o2.get_full_info())


# masala 41

# s1 = "sen nima uchun sening sen qildi"
# print(len(s1.split()))


# masala 42

# s1 = "TURT OLMA ANNA KITOB ASA"
# soz = s1.split()
# s = sum(1 for i in soz if i[0] == i[-1])
# print(s)


# masala 43

# s = "SALOM MENING ISMIM AZIZA "
# soz = s.split()
# print(sum(1 for i in soz if 'A' in i))


# masala 44

# s = "ANARA ALMA AAA GUL"
# soz = s.split()
# print(sum(1 for i in soz if i.count('A') == 3))


# masala 45

# s = "salom men ketdim"
# soz = s.split()
# print(min(len(i) for i in soz))


# masala 46

# s = "salom men ketdim"
# soz = s.split()
# print(max(len(i) for i in soz))


# masala 47

# s = "salom men ketdim"
# print("-".join(s.split()))


# masala 50

# s = "   salom   men   ketdim  "
# soz = s.split()
# print(" ".join(soz[::-1]))


# masala 51

# s = "   SALOM    MEN NIMA    QILDIM   ANOR   GUL  "
# soz = s.split()
# print(" ".join(sorted(soz)))


# masala 52

# s = "salom men ketdim"
# soz = s.split()
# new = [i.capitalize() for i in soz]
# print(" ".join(new))


# masala 53

# s = "Salom, mening ismim nima? Ha!"
# sm = 0
# for i in s:
#     if not i.isalpha() and not i.isdigit() and not i.isspace():
#         sm += 1
# print(sm)


# masala 54

# s = "Salom Mening Ismim Nima"
# d = 0
# for i in s:
#     if i.isupper():
#         d += 1
# print(d)


# masala 55

# s = "salom ketayotgan edim"
# soz = s.split()
# uzun = soz[0]
# for i in soz:
#     if len(i) > len(uzun):
#         uzun = i
# print(uzun)



# masala 56

# s = "salom ketayotgan edim"
# soz = s.split()
# uzun = soz[0]
# for i in soz:
#     if len(i) < len(uzun):
#         uzun = i
# print(uzun)


# Masala 57

# s = "salom men   nega    bu yerdaman    nega"
# print(" ".join(s.split()))


# Masala 58

# s = r"D:\Qudrat_c++\books\My_book.exe"
# soz = s.split("\\")[-1]
# d = soz.split('.')[0]
# print(d)


# Masala 59

# s = r"D:\Qudrat_c++\books\My_book.exe"
# soz = s.split("\\")[-1]
# d = soz.split('.')[1]
# print(d)


# Masala 60

# s = r"D:\Qudrat_c++\books\My_book.exe"
# soz = s.split("\\")[1]
# print(soz)


# Masala 61

# s = r"D:\Qudrat_c++\books\My_book.exe"
# soz = s.split("\\")[2]
# print(soz)


# Masala 62

# s = 'sa lom men'
# new = ""
# for i in s:
#     if i.isalpha():
#         if i == 'z':
#             new += "a"
#         elif i == "Z":
#             new += "A"
#         else:
#             new += chr(ord(i)+1)
#     else:
#         new += i
# print(new)


# Masala 63

# s = 'abcd'
# son = 2
# new = ""
# for i in s:
#     if i.isalpha():
#         if i == 'z':
#             new += 'a'
#         elif i == "Z":
#             new += "A"
#         else:
#             new += chr(ord(i)+2)
#     else:
#         new += i
# print(new)

# s = 'salom'                                    2 xil yolda ishladim
# new = ""
# for i in range(len(s)):
#     ind = s[i]
#     aniqlash = chr((ord(ind) - ord('a') + 2) % 26 + ord('a'))
#     new += aniqlash
# print(new)

# Masala 64

# s = 'ucnqo'
# son = 2
# new = ""
# for i in s:
#     if i.isalpha():
#         if i == 'z':
#             new += 'a'
#         elif i == "Z":
#             new += "A"
#         else:
#             new += chr(ord(i)-2)
#     else:
#         new += i
# print(new)


# Masala 65

# s = 'ucnqo'
# birinchi = "s"
# new = ""
# k = ord(s[0]) - ord(birinchi)
# print(k)
# for i in s:
#     new += chr(ord(i) - k)
# print(new)


# Masala 66

# s = "Programma"
# juft = ""
# toq = ""
# for i in range(len(s)):
#     if i % 2 == 0:
#         juft += s[i]
#     else:
#         toq += s[i]
# tayyor = juft + toq[::-1]
# print(tayyor)


# Masala 67

# s = "Pormamagr"
# yarm = (len(s) + 1) // 2
# juft = s[:yarm]
# toq = s[yarm:][::-1]
# tayyor = "".join(j+t for j, t in zip(juft, toq))
# if len(juft) > len(toq):
#     tayyor += juft[-1]
# print(tayyor)


# Masala 68

# s = "abcfd1243"
# d = None
# for i in s:
#     if i.isalpha() and i.islower():
#         if d is None:
#             d = i
#         else:
#             if i < d:
#                 print(i)
#                 break
#             d = i
# else:
#     print(0)




# Masala 69



# Masala 70




