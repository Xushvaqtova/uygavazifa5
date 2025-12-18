#
# class Car:
#     def __init__(self, model, year, price_per_day, status=True):
#         self.model = model
#         self.year = year
#         self._price_per_day = price_per_day
#         self.status = status
#
#     def __str__(self):
#         return f"{self.model} ({self.year})"
#
#     def get_info(self):
#         holat = "Mavjud" if self.status else "Ijarada"
#         return f"Model: {self.model}, Yili: {self.year}, Narx: {self._price_per_day}$, Status: {holat}"
#
#     @property
#     def price_per_day(self):
#         return self._price_per_day
#
#     @price_per_day.setter
#     def price_per_day(self, price):
#         self._price_per_day = price
#
#
# class Customer:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.rented_cars = []
#
#     def __str__(self):
#         return self.name
#
#     def get_info(self):
#         return f"Ismi: {self.name}, Yoshi: {self.age}, Manzili: {self.address}"
#
#     def get_cars(self):
#         if not self.rented_cars:
#             return f"{self.name} hali mashina ijaraga olmagan."
#         return f"{self.name} ijaraga olgan mashinalar: " + ", ".join([i.model for i, j, k in self.rented_cars])
#
#     def get_all_price(self):
#         x = sum(price for i, j, price in self.rented_cars)
#         return f"Umumiy to‘lov: {x}$"
#
#
# class RentalSystem:
#     def __init__(self, name):
#         self.name = name
#         self.cars = []
#         self.rents = []
#
#     def add_cars(self, car):
#         self.cars.append(car)
#         print(f"{car.model} mashina qoshildi.")
#
#     def delete_car(self, car_model):
#         car = [i for i in self.cars if i.model == car_model]
#         if car:
#             self.cars.remove(car[0])
#             print(f"{car_model} mashina ochirildi.")
#         else:
#             print("Bu model yoq bizda.")
#
#     def update_car(self, old_car, new_car):
#         if old_car in self.cars:
#             self.cars.remove(old_car)
#             self.cars.append(new_car)
#             print(f"{old_car.model} orniga {new_car.model} yangilandi")
#
#
#     def borrowed_cars(self, car, day, customer):
#         car_ = [i for i in self.cars if i.model == car.model and i.status is True]
#         if car_:
#             car.status = False
#             summa = car.price_per_day * day
#             self.rents.append([car, day, customer])
#             customer.rented_cars.append((car, day, summa))
#             print(f"{customer.name} {car.model} ni {day} kunga ijaraga oldi. Narx: {summa}$")
#         else:
#             print("Bu model hozirda ijarada.")
#
#
#     def get_rents(self):
#         if not self.rents:
#             print("Hozircha ijarada mashina yo q.")
#             return
#         for car, days, cust in self.rents:
#             print(f"{car.model} — {cust.name}, {days} kun")
#
#
#
# car1 = Car("Malibu", 2022, 100)
# car2 = Car("K5", 2021, 80)
#
# customer1 = Customer("Madina", 25, "Toshkent")
# system = RentalSystem("SuperRent")
#
# # system.add_cars(car1)
# # system.add_cars(car2)
#
# system.borrowed_cars(car1, 3, customer1)
#
# system.get_rents()
# print(customer1.get_cars())
# print(customer1.get_all_price())
#
# system.get_rents()










# Array 47

# n = [2, 3, 4, 5, 6,1, 8, 2, 3, 6, 4, 5,7]
# new = []
# for i in n:
#     if i not in new:
#         new.append(i)
# print(new)


# Array 48

# n = [2, 4, 3, 4, 6, 3, 4, 3, 1, 7]
# s = 0
# for i in n:
#     d = n.count(i)
#     if d > s:
#         s = d
# print(s)


# Array 49

# n = [1, 2, 3, 4, 6, 1, 9, 4]
# ind = -1
# for i in range(len(n)):
#     if not (1 <= n[i] <= len(n)):
#         ind = i
#         break
# if ind == -1:
#     print(0)
# else:
#     print(ind)


# Array 50

# a = [7, 4, 2, 3, 1, 5]
# n = len(a)
# new = []
# for i in range(n - 1):
#     if a[i] > a[i + 1]:
#         new.append(a[i])
# print(new)


# Array 51

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# a, b = b, a
# print("A-", a, '\n', "B-", b)


# Array 52

# n = [7, 2, 3, 6, 9, 11]
# b = []
# for i in n:
#     if i < 5:
#         b.append(2 * i)
#     else:
#         b.append(i / 2)
# print(b)


# Array 53

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# c = []
# c.append(max(a))
# c.append(max(b))
# print(c)


# Array 54

# n = [1, 2, 3, 4, 5, 6, 8]
# new = []
# for i in n:
#     if i % 2 == 0:
#         new.append(i)
# print(f"Yangi - {new}, uzunligi: {len(new)}")


# Array 55

# n = [1, 2, 9, 7, 3, 8]
# new = []
# for i in range(1, len(n), 2):
#     new.append(n[i])
# print(f"Yangi - {new}, uzunligi: {len(new)}")


# Array 56

# n = [1, 2, 9, 7, 3, 8, 5, 6, 7, 9, 5]
# new = []
# for i in range(0, len(n), 3):
#     new.append(n[i])
# print(f"Yangi - {new}, uzunligi: {len(new)}")


# Array 57

# n = [1, 2, 3, 4, 5, 6, 7]
# s = [i for i in range(len(n)) if i % 2 == 0] + [i for i in n if i % 2 != 0]
# print(s)


