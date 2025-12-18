class Dish:
    def __init__(self, name, price, timeprp):
        self.name = name
        self.price = price
        self.timeprp = timeprp

    def get_info(self):
        return self.name, self.price, self.timeprp

    @property
    def get_price(self):
        return self.price

    def set_price(self,name,price):
        if self.name==name:
            self.price=price

class Customer:
    def __init__(self,name,address):
        self.name = name
        self.address = address

    def get_info(self):
        return self.name, self.address


class Menu:
    def __init__(self,name):
        self.name = name
        self.dishes=[]
        self.dish_num=0

    def add_dish(self,dish):
        self.dishes.append(dish)
        self.dish_num+=1

    def remove_dish(self,dish):
        for i in self.dishes:
            if i.name==dish:
                self.dishes.remove(i)
                self.dish_num-=1
                break

class Order:
    def __init__(self,id):
        self.id=id
        self.card={}

    def get_menyu(self):
        for i in self.dishes:
            return i.name, i.price, i.timeprp

    def add_dish(self,user,dish):
        if user not in self.card:
            self.card[user]=[]
        self.card[user].append(dish)

    def remove_dish(self,user,dish):
        if user in self.card:
            if dish in self.card[user]:
                self.card[user].remove(dish)
                if not self.card[user]:
                    del self.card[user]

    def calculate_total(self):
        total=0
        for dishes in self.card.values():
            for i in dishes:
                total+=i.price
        return total

d1=Dish('Sushi',300,'30min')
d2=Dish('Plov',5000,'1h')

c1= Customer('Joji','Newyrk')
c2=Customer('Jack','Newyrk')

m=Menu('Bar')
m.add_dish(d1)
m.add_dish(d2)

o1 = Order(1)
o1.add_dish(c1,d1)
o1.add_dish(c1,d2)
o1.add_dish(c2,d1)
print(o1.calculate_total())


# class 2

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



