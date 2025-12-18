# class 1


# class Car:
#     def __init__(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year = year
#
#     def get_info(self):
#         return f"\n Nomi: {self.name}\n Modeli: {self.model}\n Yili: {self.year}"
#
# c1 = Car("BMW", "M5", 2024)
# c2= Car("Audi", "x2", 2020)
#
# print(c1.get_info())
# print(c2.name)





# class 2
#
# class Car:
#     def __init__(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year = year
#
#     def get_info(self):
#         return f"\n Nomi: {self.name}\n Modeli: {self.model}\n Yili: {self.year}"
#
#
# class ElectroCar(Car):
#     def __init__(self, name, model, year, batarey, mil):
#         Car.__init__(self, name, model, year)
#         self.batarey = batarey
#         self.mil = mil
#
#     def get_electro_info(self):
#         return f"{self.get_info()}\n batareyasi: {self.batarey}\n Mil: {self.mil}"
#
#
#
# c1 = Car("BMW", "M5", 2024)
# e1= ElectroCar("Audi", "x2", 2020, 99, 2000)
#
# print(c1.get_info())
# print(e1.get_electro_info())





# class 3

# class Car:
#     def __init__(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year = year
#
#     def get_info(self):
#         return f"\n Nomi: {self.name}\n Modeli: {self.model}\n Yili: {self.year}"
#
#
# class Salon:
#     def __init__(self, nomi, adress):
#         self.nomi = nomi
#         self.adres = adress
#
#     def get_salon_info(self):
#         return f"\n Nomi: {self.nomi}\n manzil: {self.adres}"
#
# class Xaridor(Car, Salon):
#     def __init__(self, name, model, year, nomi, adress, ism, yosh):
#         Car.__init__(self, name, model, year)
#         Salon.__init__(self, nomi, adress)
#         self.ism = ism
#         self.yosh = yosh
#
#     def get_info_xaridor(self):
#         return f"{self.get_info()} {self.get_salon_info()}\n ism: {self.ism}\n yoshi: {self.yosh}"
#
#
# c1 = Car("BMW", "M5", 2024)
# s1= Salon("Yoshlik", "MOjiza")
# x1 = Xaridor("BYD", "Song plus", 2024, "Bebaho","Qunz",  "Ulugbek", 22)
#
# print(c1.get_info())
# print(s1.get_salon_info())
# print(x1.get_info_xaridor())






# class 4

# class Talaba:
#     def __init__(self, name, age, id):
#         self.name = name
#         self.id = id
#         self.age = age
#
#     def get_info(self):
#         return f"\n Ismi: {self.name}\n Yoshi: {self.age}\n Id: {self.id}"
#
#
# class Centr:
#     def __init__(self, nomi, manzil):
#         self.nomi = nomi
#         self.manzil = manzil
#         self.talaba_soni = 0
#         self.talabalar = []
#
#     def add_talaba(self, talaba):
#         self.talaba_soni += 1
#         self.talabalar.append(talaba)
#
#     def get_info_talaba(self):
#         for i in self.talabalar:
#             print(i.get_info())
#
# t1 = Talaba("Azim",20, 12345)
# t2 = Talaba("Ali",22, 34567)
# t3 = Talaba("Salim",23, 876545)
#
# c1 = Centr("NT", "Qoraqamish")
#
# c1.add_talaba(t1)
# c1.add_talaba(t2)
# c1.add_talaba(t3)
#
# c1.get_info_talaba()
# print(c1.talaba_soni)







# class 5


# class Car:
#     def __init__(self, name, model, year, color, id, count, price):
#         self.name = name
#         self.model = model
#         self.year = year
#         self.color = color
#         self.id = id
#         self.count = count
#         self.price = price
#
#     def set_count_car(self, count):
#         self.count = count
#
#     def set_color_car(self, ncolor):
#         self.color = ncolor
#
#     def get_all_price_car(self):
#         return self.price * self.count
#
#     def get_info(self):
#         return f"\n Nomi: {self.name}\n Modeli: {self.model}\n Yili: {self.year}\n Rangi: {self.color}\n Id: {self.id}\n Soni: {self.count}\n Narxi: {self.price}"
#
#
# class Salon:
#     def __init__(self, nomi, adress):
#         self.nomi = nomi
#         self.adress = adress
#         self.car_count = 0
#         self.cars = []
#
#     def add_car(self, car):
#         self.car_count += 1
#         self.cars.append(car)
#
#     def info_car(self):
#         print({self.car_count})
#         for i in self.cars:
#             print(i.get_info())
#
#     def by_car(self, id, count):
#         try:
#             car = [i for i in self.cars if i.id == id][0]
#         except Exception:
#             return "Siz kiritgan id da mashina yoq"
#         if car.count < count:
#             return f"salonimizda faqat {car.count} ta bor xolos"
#         car.count -= count
#         return f" {count} ta {car.model} oldingiz"
#
#
#     def filter_by_color(self, color):
#         car = [i.get_info() for i in self.cars if i.color == color]
#         return car if len(car) > 0 else "bunday ranglisi yoq"
#
#     def filter_by_id(self, id):
#         car = [i for i in self.cars if i.id == id][0]
#         return f"{car.model} dan {car.count} ta bor"
#
#     def filter_by_price(self, minpr, maxpr):
#         car = [i.get_info() for i in self.cars if minpr <= i.price <= maxpr]
#         return car if len(car) > 0 else "Bunday narxda mashina yoq"
#
#     def get_all_price(self):
#         return f"Salonda {sum([i.count for i in self.cars])} mashina bor. Umumiy narxi: {sum([i.get_all_price_car() for i in self.cars])}"
#
#
# c1 = Car("BMW", "M5", 2024, "blue", 1234, 4, 22000)
# c2= Car("Audi", "x2", 2020, "red", 543, 8, 34000)
#
# s1 = Salon("Gozal", "Qoqon")
#
# s1.add_car(c1)
# s1.add_car(c2)

# s1.info_car()
# print(s1.car_count)
# print(s1.filter_by_color("yellow"))
# print(s1.filter_by_id(1234))
# print(s1.filter_by_price(5000, 400000))
# print(s1.get_all_price())
# print(s1.by_car(543, 2))







# class 6


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_info_student(self):
#         return f"\n Name: {self.name}\n Age: {self.age}"
#
# class Teacher:
#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject
#         self.groups = []
#
#     def add_group(self, new_group):
#         self.groups.append(new_group)
#
#     def delete_group(self, group_name):
#         self.groups.remove(group_name)
#
#     def update_group(self, new_name, old_name):
#         if old_name in self.groups:
#             i = self.groups.index(old_name)
#             self.groups[i] = new_name
#
#     def get_info_teacher(self):
#         return f"\n Oqituvchi ismi: {self.name}\n Fani: {self.subject}\n Guruhlari: {self.groups}"
#
#
# class Groups:
#     def __init__(self, name):
#         self.name = name
#         self.students = []
#
#     def get_info_group(self):
#         student_list = [i.get_info_student() for i in self.students]
#         return f"\n Guruh nomi: {self.name}\n Oquvchilar:\n" + "\n".join(student_list)
#
#     def add_student(self, new_student):
#         self.students.append(new_student)
#
#     def delete_student(self, student_name):
#         for i in self.students:
#             if i.name == student_name:
#                 self.students.remove(i)
#                 break
#
#     def update_student(self, old_sname, new_snmae, new_age):
#         for i in self.students:
#             if i.name == old_sname:
#                 i.name = new_snmae
#                 i.age = new_age
#                 break
#
#     def count_student(self):
#         return len(self.students)
#
# s1 = Student("Madina", 22)
# s2 = Student("Noila", 21)
# s3 = Student("Asila", 23)
#
# g1 = Groups("Python")
# g1.add_student(s1)
# g1.add_student(s2)
# g1.add_student(s3)
#
# t1 = Teacher("Azim", "Python")
# t1.add_group("python n72")


# print(t1.get_info_teacher())
# print("---------------------------------------------------")
# print(g1.get_info_group())
# print("Talabalar soni: ", g1.count_student())
# g1.update_student("Noila", "Azima", 25)
# print(g1.get_info_group())
# g1.delete_student("laziza")
# print(g1.get_info_group())












# class 7

# class Student:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#     def get_info_student(self):
#         return f"\n Name: {self.name}\n Age: {self.age}\n Address: {self.address}"
#
#
# class Course:
#     def __init__(self, title, teacher_name):
#         self.title = title
#         self.teacher_name = teacher_name
#         self.students = []
#
#     def add_student(self, student):
#         return self.students.append(student)
#
#     def remove_student(self, student):
#         for s in self.students:
#             if s.name == student:
#                 self.students.remove(s)
#                 break
#
#     def list_students(self):
#         st = [i.get_info_student() for i in self.students]
#         return st if len(st) > 0 else "Talabalar yoq"
#
#     def get_info_course(self):
#         return f"\n Title: {self.title}\n Teacher_name: {self.teacher_name}\n Students: {len(self.students)}"
#
# class Platform:
#     def __init__(self, name):
#         self.name = name
#         self.courses = []
#
#     def add_course(self, course):
#         return self.courses.append(course)
#
#     def remove_course(self, title):
#         for i in self.courses:
#             if i.title == title:
#                 return self.courses.remove(i)
#
#
#     def list_courses(self):
#         cs = [i.get_info_course() for i in self.courses]
#         return cs if len(cs) > 0 else "Platformada curs yoq hozircha"
#
#     def get_all_students(self):
#         all_student = []
#         for i in self.courses:
#             all_student.extend(i.students)
#             return [i.get_info_student() for i in all_student]
#
# s1 = Student("Asila", 18, "Toshkent")
# s2 = Student("Vali", 20, "Samarqand")
# s3 = Student("Madina", 22, "Fargona")
#
#
# c1 = Course("Python", "Akmal")
# c2 = Course("Web", "Zafar")
#
# c1.add_student(s1)
# c1.add_student(s2)
# c2.add_student(s3)
#
#
# p1 = Platform("IT Platforma")
# p1.add_course(c1)
# p1.add_course(c2)
#
# for i in p1.list_courses():
#     print(i)
#
# c1.remove_student("Vali")
# for i in c1.list_students():
#     print(i)
#
# for i in p1.get_all_students():
#     print(i)
#
# p1.remove_course("Web")
# for i in p1.list_courses():
#     print(i)








# class 8

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
#         return f"Modeli: {self.model}\n Yili: {self.year}\n Narx: {self._price_per_day}$\n Status: {holat}"
#
#     @property
#     def price_per_day(self):
#         return self._price_per_day
#
#     @price_per_day.setter
#     def price_per_day(self, price):
#         self._price_per_day = price
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
#             return f"{self.name} hali mashina ijaraga olinmagan"
#         return f"{self.name} ijaradagi mashinalar: " + ", ".join([i.model for i, j, k in self.rented_cars])
#
#     def get_all_price(self):
#         x = sum(price for i, j, price in self.rented_cars)
#         return f"Umumiy tolov: {x}$"
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
#         print(f"{car.model} mashina qoshldi")
#
#     def delete_car(self, carmodel):
#         car = [i for i in self.cars if i.model == carmodel]
#         if car:
#             self.cars.remove(car[0])
#         else:
#             print("Bu model bizda yoq")
#
#     def update_car(self, old_car, new_car):
#         if old_car in self.cars:
#             self.cars.remove(old_car)
#             self.cars.append(new_car)
#             print(f"{old_car.model} orniga {new_car.model} qoshildi")
#
#     def borrowed_cars(self, car, day, customer):
#         car_ = [i for i in self.cars if i.model == car.model and i.status is True]
#         if car_:
#             car.status = False
#             summa = car.price_per_day * day
#             self.rents.append([car, day, customer])
#             customer.rented_cars.append((car, day, summa))
#             print(f"{customer.name} {car.model}ni {day} kunga ijaraga oldi. Narxi: {summa}$")
#         else:
#             print("Bu model xozirda yoq")
#
#     def get_rents(self):
#         if not self.rents:
#             print("Hozircha ijarada mashina yoq")
#             return
#         for car, days, cust in self.rents:
#             print(f"{car.model} - {cust.name}, {days} kun")
#
# car1 = Car("Malibu", 2022, 100)
# car2 = Car("K5", 2021, 80)
#
# c1 = Customer("Madina", 25, "Toshkent")
# r = RentalSystem("SuperRent")
#
# r.add_cars(car1)
# r.add_cars(car2)
# r.borrowed_cars(car1, 2, c1)
# r.get_rents()
# print(c1.get_cars())
# print(c1.get_all_price())






# class 9


# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#     def __str__(self):
#         return f"Turi: {self.title}\n Aftor: {self.author}\n Yili: {self.year}"
#
#
# class Reader:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#         self.borowwed_books = []
#
#     def boroww_book(self, book):
#         self.borowwed_books.append(book)
#         print(f"{self.name} oldi: {book.title}")
#
#     def return_book(self, book):
#         if book in self.borowwed_books:
#             self.borowwed_books.remove(book)
#             print(f"{self.name} kitobni qaytardi: {book.title}")
#         else:
#             print(f"{book.title} sizda kitob yoq")
#
#     @property
#     def borrowed_count(self):
#         return len(self.borowwed_books)
#
#
# class Library:
#     books = []
#
#     def __init__(self):
#         pass
#
#     def add_book(self, book):
#         Library.books.append(book)
#         print(f"Kutubxonaga kitob qoshildi: {book.title}")
#
#     def remove_book(self, book):
#         if book in Library.books:
#             Library.books.remove(book)
#             print(f"kitob olib tashlandi: {book.title}")
#         else:
#             print(f"{book.title} bunday kitob yoq")
#
#     @classmethod
#     def total_books(cls):
#         return len(cls.books)
#
#
# book1 = Book("Alkimyogar", "Paulo Coelho", 1988)
# book2 = Book("1984", "Jorj Oruell", 1949)
# book3 = Book("O‘tkan kunlar", "Abdulla Qodiriy", 1925)
#
# library = Library()
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
#
# print(library.total_books())
#
# reder = Reader("LOla", 12345)
# reder.boroww_book(book3)
# print(reder.borrowed_count)
# print(reder.return_book(book3))




# class Dish:
#     def __init__(self, name, price,timeprp):
#         self.name = name
#         self.price = price
#         self.timeprp = timeprp
#
#     def get_info(self):
#         return self.name, self.price, self.timeprp
#
#     @property
#     def get_price(self):
#         return self.price
#
#     def set_price(self,name,price):
#         if self.name==name:
#             self.price=price
#
# d1=Dish('Sushi',300,'30min')
# d2=Dish('Plov',5000,'1h')
#
#
# class Customer:
#     def __init__(self,name,address):
#         self.name = name
#         self.address = address
#
#     def get_info(self):
#         return self.name, self.address
#
# c1= Customer('Joji','Newyrk')
# c2=Customer('Jack','Newyrk')
#
#
# class Menu:
#     def __init__(self,name):
#         self.name = name
#         self.dishes=[]
#         self.dish_num=0
#
#     def add_dish(self,dish):
#         self.dishes.append(dish)
#         self.dish_num+=1
#
#     def remove_dish(self,dish):
#         for i in self.dishes:
#             if i.name==dish:
#                 self.dishes.remove(i)
#                 self.dish_num-=1
#                 break
#
# menyu=Menu('Bar')
# menyu.add_dish(d1)
# menyu.add_dish(d2)
#
# class Order:
#     def __init__(self,id):
#         self.id=id
#         self.card={}
#
#     def get_menyu(self):
#         for i in self.dishes:
#             return i.name, i.price, i.timeprp
#
#     def add_dish(self,user,dish):
#         if user not in self.card:
#             self.card[user]=[]
#         self.card[user].append(dish)
#
#     def remove_dish(self,user,dish):
#         if user in self.card:
#             if dish in self.card[user]:
#                 self.card[user].remove(dish)
#                 if not self.card[user]:
#                     del self.card[user]
#
#     def calculate_total(self):
#         total=0
#         for dishes in self.card.values():
#             for i in dishes:
#                 total+=i.price
#
#         return total
#
#     def vieworder(self):
#         new = {}
#         for key, value in self.card.items():
#             new[key.name]=[v.name for v in value]
#         return new
# o1 = Order(1)
# o1.add_dish(c1,d1)
# o1.add_dish(c1,d2)
# o1.add_dish(c2,d1)
# print(o1.calculate_total())


# Electron kundalik
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def get_info(self):
#         return self.name,self.age
# class Teacher:
#     def __init__(self,name,subject):
#         self.name=name
#         self.subject=subject
#
#     def get_info(self):
#         return self.name,self.subject
#
#
# class Group:
#     def __init__(self,name,students,teacher):
#         self.name=name
#         self.students=[]
#         self.teacher=teacher
#
#     def get_info(self):
#         return self.name,self.students,self.teacher
#
#     def add(self,student):
#         self.students.append(student)
#
#     def remove(self,name):
#         for i in self.students:
#             if i.name==name:
#                 self.students.remove(i)
#                 break
#
#     def get_students(self):
#         for i in self.students:
#             return i
#
# t1 = Teacher("Mr. Ali", "Math")
#
# s1 = Student("Aziz", 16)
# s2 = Student("Malika", 17)
# s3 = Student("Sardor", 16)
#
# g1 = Group("10A", t1)
# g1.add(s1)
# g1.add(s2)
# g1.add(s3)
#
# print(t1.info())
# print(s1.info())
# print(g1.info())
#
# g1.remove("Malika")
#
# print("Students now:", g1.get_students())



#Internet Dokoni
# class Category:
#     def __init__(self,name):
#         self.name=name
#
#     def __str__(self):
#         return f'category: {self.name}'
#
# class Product:
#     def __init__(self,name,price,category):
#         self.name=name
#         self.price=price
#         self.category=category
#
#     def __str__(self):
#         return f'{self.name},{self.category.name},{self.price}'
#
# class User:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def get_info(self):
#         return self.name,self.age
#
#     def get_order(self,cart):
#         if self.name in cart.products:
#             for i in cart.products[self.name]:
#                 return i.name
#         else:
#             return []
#
#
# class Cart:
#     def __init__(self):
#         self.products={}
#
#     def add_product(self,user,product):
#         if user.name not in self.products:
#             self.products[user.name]=[]
#             self.products[user.name].append(product)
#
#
#     def remove_product(self,user,product):
#         if user.name in self.products:
#             for i in self.products[user.name]:
#                 if i.name==product:
#                     self.products[user.name].remove(i)
#                     break
#
#     def total_price(self,user):
#         if user.name in self.products:
#             return sum(i.price for i in self.products[user.name])
#
# c1 = Category("Electronics")
# c2 = Category("Clothes")
#
# p1 = Product("iPhone", 15000000, c1)
# p2 = Product("T-shirt", 120000, c2)
# p3 = Product("Laptop", 9000000, c1)
#
# u1 = User("Aziz", 18)
# u2 = User("Malika", 20)
# cart = Cart()
#
# cart.add_product(u1, p1)
# cart.add_product(u1, p2) b  ??
# cart.add_product(u2, p3)
# cart.add_product(u1, p2)
#
# print(u1.get_info())
# print("🛒 Заказ:", u1.get_order(cart))
# print("💰 Общая сумма:", cart.total_price(u1))
#
# print()
# print(u2.get_info())
# print("🛒 Заказ:", u2.get_order(cart))
# print("💰 Общая сумма:", cart.total_price(u2))
#
# cart.remove_product(u1, "T-shirt")
# print(u1.get_order(cart))






















