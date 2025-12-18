# class 1


# class Car:
#     def __init__(self, id, make, model, color, price, count):
#         self.id = id
#         self.make = make
#         self.model = model
#         self.color= color
#         self.price = price
#         self.count = count
#
#     def set_count_car(self, count):
#         self.count = count
#
#     def set_color_car(self, new_color):
#         self.color = new_color
#
#     def get_info_car(self):
#         return f" IDsi: {self.id} Ishlangan joyi: {self.make} Modeli: {self.model} Rangi: {self.color} Narxi: {self.price} Soni: {self.count}"
#
#     def get_car_all_price(self):
#         return self.price + self.count
#
#
# class AvtoSalon:
#     def __init__(self, name):
#         self.name = name
#         self.count_car = 0
#         self.cars = []
#
#     def add_car(self, car):
#         self.count_car += 1
#         self.cars.append(car)
#
#     def get_info(self):
#         print(f"Mashina soni {self.count_car}")
#         for i in self.cars:
#             print(i.get_info_car())
#
#     def by_car(self, id, count):
#         try:
#             car = [i for i in self.cars if i.id == id][0]
#         except Exception:
#             return "Siz kiritga id da mashina topilmadi"
#         if car.count < count:
#             return f"Bizda bu mashinadan {car.count} ta bor xolos"
#         car.count -= count
#         return f"Siz {count} ta {car.model} oldingiz"
#
#     def filter_color_cars(self, color):
#         cars = [i.get_info_car() for i in self.cars if i.color == color]
#         return cars if len(cars) > 0 else "Siz tanlagan rangdagi mashina yoq"
#
#     def get_car(self, id):
#         car = [i for i in self.cars if i.id == id][0]
#         return f"{car.model} dan {car.count} ta bor"
#
#     def get_all_price(self):.
#         return f"Sizning avtosaloningizda {self.count_car} ta model bor, {sum([i.count for i in self.cars])} ta mashina bor. Umumiy summasi: {sum([i.get_car_all_price() for i in self.cars])}"
#
#     def filter_by_price(self, min_price, max_price):
#         cars = [i.get_info_car() for i in self.cars if min_price <= i.price <= max_price]
#         return cars if cars else "Bu oraliqda mashina yo'q"
#
# c1 = Car(1, "BMW", "M5", "OQ", 21000, 3)
# c2 = Car(2, "AUDI", "X5", "Qora", 12000, 2)
# c3 = Car(3, "BYD", "Song plus", "Kok", 13000, 1)
# c4 = Car(4, "Porsche", "Sedan", "Qora", 31000, 4)
#
# a1 = AvtoSalon("Motobika")
#
# a1.add_car(c1)
# a1.add_car(c2)
# a1.add_car(c3)
# a1.add_car(c4)

# print(c1.get_car_all_price())

# c2.set_count_car(5)
#
# print(a1.by_car(1, 3))
# print(a1.by_car(2, 1))
#
# print(a1.get_car(2))
#
# print(a1.filter_color_cars("Qora"))

# print(a1.filter_by_price(10000, 25000))
# print(a1.get_all_price())



# class 2

# class Dori:
#     def __init__(self, id, name, type, country, price, count):
#         self.id = id
#         self.name = name
#         self.type = type
#         self.country = country
#         self.price = price
#         self.count = count
#
#     def get_info_dori(self):
#         return f"ID: {self.id}, Nomi: {self.name}, Turi: {self.type}, Ishlab chiqarilgan joyi: {self.country}, Narxi: {self.price}$, Soni: {self.count} dona"
#
#     def get_all_price(self):
#         return self.price * self.count
#
#
# class Apteka:
#     def __init__(self, name):
#         self.name = name
#         self.count_dori = 0
#         self.dorilar = []
#
#     def add_medicine(self, medicine):
#         self.count_dori += 1
#         self.dorilar.append(medicine)
#
#     def get_info(self):
#         print(f"Aptekada {self.count_dori} xil dori mavjud")
#         for med in self.dorilar:
#             print(med.get_info_dori())
#
#     def filter_by_country(self, country):
#         meds = [m.get_info_dori() for m in self.dorilar if m.country == country]
#         return meds if meds else f"{country}da ishlab chiqarilgan dori topilmadi"
#
#     def get_dori(self, id):
#         med = [i for i in self.dorilar if i.id == id][0]
#         return f"{med.name} dorisidan {med.count} dona mavjud"
#
#     def get_all_price(self):
#         all_count = sum([m.count for m in self.dorilar])
#         all_price = sum([m.get_all_price() for m in self.dorilar])
#         return f"{self.count_dori} xil dori, {all_count} dona dori bor. Umumiy qiymati: {all_price}$"
#
#
# m1 = Dori(1, "Paracetamol", "Tabletka", "Xitoy", 2, 50)
# m2 = Dori(2, "Nurofen", "Sirop", "Italiya", 5, 20)
# m3 = Dori(3, "Vitamin C", "Tabletka", "O‘zbekiston", 3, 100)
# m4 = Dori(4, "Amoxicillin", "In'eksiya", "Germaniya", 10, 10)
#
# pharmacy = Apteka("Shifo Aptekasi")
#
# pharmacy.add_medicine(m1)
# pharmacy.add_medicine(m2)
# pharmacy.add_medicine(m3)
# pharmacy.add_medicine(m4)
#
# # print(pharmacy.get_dori(2))
# # print(pharmacy.filter_by_country("Xitoy"))
# print(pharmacy.get_all_price())




# class 3


# class Suv:
#     def __init__(self, name, price, length, color):
#         self.name = name
#         self.price = price
#         self.length = length
#         self.color = color
#
#     def get_info(self):
#         return f"Nomi: {self.name}, Narxi: {self.price} so'm, Hajmi: {self.length}, Rangi: {self.color}"
#
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
#     def filter_by_color(self, color):
#         result = [i.get_info() for i in self.suvlar if i.color == color]
#         return result if result else f"{color} rangdagi suv mavjud emas"
#
#
# w1 = Suv("Fanta", 9000, "0.5 litr", "Ko'k")
# w2 = Suv("Sprite", 11000, "1 litr", "Yashil")
# w3 = Suv("Dena", 15000, "1.5 litr", "Ko'k")
#
# d1 = Dokon("Zeydil", "Mirobod")
#
# d1.add_water(w1)
# d1.add_water(w2)
# d1.add_water(w3)
#
# # d1.get_water()
#
# print(d1.filter_by_color("Ko'k"))
# print(d1.filter_by_color("Qizil"))





















# Masala 1

# n = [2, 7, 4, 9, 1, 3]
# s = n[-1]
# res = 0
# for i in n:
#         if i < s:
#             res = i
#             break
# print(res)


# Masala 2

# n = [3, 9, 5, 12, 8, 15]
# s = n[-1]
# k = n[0]
# res = 0
# for i in reversed(range(len(n))):
#         if k < n[i] < s:
#             res = i
#             break
# print(res)


# Masala 3

# n = [3, 9, 5, 12, 8, 15, 2, 7, 4, 9, 1, 3]
# k = 2
# l = 6
# s = 0
# for i in range(k, l+1):
#     s += n[i]
# print(s)


# Masala 4

# n = [3, 9, 5, 12, 8, 15, 9]
# k = 2
# l = 6
# s = 0
# for i in range(k, l+1):
#     s += n[i]
# d = s / (l - k + 1)
# print(d)


# Masala 5

# n = [3, 9, 5, 12, 8, 15, 2, 7, 4, 9, 1, 3]
# k = 2
# l = 6
# s = 0
# s += (sum(n[:k]) + sum(n[l:])) / (len(n[:k]) + len(n[l:]))
# print(s)
































