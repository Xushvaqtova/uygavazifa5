
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
#     def get_all_price(self):
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
# # print(c1.get_car_all_price())
#
# a1 = AvtoSalon("Motobika")
#
# a1.add_car(c1)
# a1.add_car(c2)
# a1.add_car(c3)
# a1.add_car(c4)

# c2.set_count_car(5)
#
# print(a1.by_car(1, 3))
# print(a1.by_car(2, 1))
#
# print(a1.get_car(2))
#
# print(a1.filter_color_cars("Qora"))

# print(a1.filter_by_price(10000, 25000))














# class Book:
#     def __init__(self, name, author, price, isbn, count):
#         self.name = name
#         self._author = author
#         self.price = price
#         self.isbn = isbn
#         self._count = count
#
#     @property
#     def count(self):
#         return self._count
#
#     @count.setter
#     def count(self, c):
#         self._count += c
#
#     @count.deleter
#     def count(self):
#         print("ochdi")
#         self._count = 0
#
#     @property
#     def author(self):
#         return self._author
#
#
#
# b1 = Book("O'tgan kunlar", 'Abdulla Qodiriy', 154000, 655521, 10)
# b2 = Book("Shum bola", 'Gafur Gulom', 70000, 655321, 110)
# b3 = Book("Otabek va Kushum", 'Abdulla oka', 75000, 655320, 11)
# b4 = Book("Python", 'Anvar Narzullayev', 1540000, 655521, 101)
#
# # b1.count = 23
# # print(b1.count)
#
# del b1.count
# print(b3.author)





class Car:
    def __int__(self, model, make, price_per_day):
        self.model = model
        self.make = make
        self.price_per_day = price_per_day

    def get_info(self):
        return  f"Model: {self.model}, Make: {self.make}, Price: {self.price_per_day}"


class RentalSystem:
    def __init__(self, name, cars):
        self.name = name
        self.cars = cars

    def add_cars(self):
        return












































