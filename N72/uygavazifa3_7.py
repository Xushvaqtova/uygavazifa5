

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_info(self):
#         return f" Talaba ism: {self.name}\n Yosh: {self.age}\n"
#
#
# class Teacher:
#     def __init__(self, name, subjects):
#         self.name = name
#         self.subjects = subjects
#         self.groups = []
#
#     def add_group(self, group_name):
#         self.groups.append(group_name)
#
#     def delete_group(self, group_name):
#         self.groups.remove(group_name)
#
#     def update_group(self, old_name, new_name):
#         if old_name in self.groups:
#             i = self.groups.index(old_name)
#             self.groups[i] = new_name
#
#     def get_info(self):
#         return f" Oqituvchi ismi: {self.name}\n Yosh: {self.subjects}\n Guruhlari: {self.groups}\n"
#
#
# class Groups:
#     def __init__(self, name):
#         self.name = name
#         self.talabalar = []
#
#     def get_info(self):
#         student_list = [i.get_info() for i in self.talabalar]
#         return f"Guruh nomi: {self.name}\n Talabalar ismi:\n" + "\n".join(student_list)
#
#     def add_students(self, talaba):
#         self.talabalar.append(talaba)
#
#     def delete_student(self, student_name):
#         for i in self.talabalar:
#             if i.name == student_name:
#                 self.talabalar.remove(i)
#                 break
#
#     def update_student(self, old_name, new_name, new_age):
#         for i in self.talabalar:
#             if i.name == old_name:
#                 i.name = new_name
#                 i.age = new_age
#                 break
#
#     def count_student(self):
#         return len(self.talabalar)
#
#
#
# s1 = Student("Madina", 19)
# s2 = Student("Ali", 12)
# s3 = Student("Aslzoda", 23)
#
#
# g1 = Groups("Python N72")
# g1.add_students(s1)
# g1.add_students(s2)
# g1.add_students(s3)
#
#
# t1 = Teacher("Lola", "Python")
# t1.add_group("Python N72")
#
#
# print(t1.get_info())
# print("-------------------------")
# print(g1.get_info())
# print("Talabalar soni: ", g1.count_student())
#
#
# g1.update_student("Noiba", "Nasiba", 22)
# print("-------------------------")
# print(g1.get_info())
# g1.delete_student("Ali")
# print("-------------------------")
# print(g1.get_info())
# print("Talabalar soni: ", g1.count_student())
# print("-------------------------")












class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_info(self):
        return f"Talaba ismi: {self.name}, Yoshi: {self.age}, Manzil: {self.address}"


class Course:
    def __init__(self, title, teacher_name):
        self.title = title
        self.teacher_name = teacher_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_name):
        for s in self.students:
            if s.name == student_name:
                self.students.remove(s)
                break

    def list_students(self):
        return [s.get_info() for s in self.students]

    def get_info(self):
        return f"Kurs nomi: {self.title}, Oqituvchi: {self.teacher_name}, Talabalar soni: {len(self.students)}"


class Platform:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, title):
        for i in self.courses:
            if i.title == title:
                self.courses.remove(i)
                break

    def list_courses(self):
        return [c.get_info() for c in self.courses]


    def get_all_students(self):
        all_students = []
        for course in self.courses:
            all_students.extend(course.students)
        return [s.get_info() for s in all_students]


s1 = Student("Asila", 18, "Toshkent")
s2 = Student("Vali", 20, "Samarqand")
s3 = Student("Madina", 22, "Fargona")


c1 = Course("Python", "Akmal")
c2 = Course("Web", "Zafar")


c1.add_student(s1)
c1.add_student(s2)
c2.add_student(s3)


p1 = Platform("IT Platforma")
p1.add_course(c1)
p1.add_course(c2)

# print("------------------------------------------------------------")
#
# print("Kurslar royxati:")
# for i in p1.list_courses():
#     print(i)
# print("------------------------------------------------------------")
#
# print("\n Python kursidagi talabalar:")
# for i in c1.list_students():
#     print(i)
# print("------------------------------------------------------------")

# print("\n Platformadagi barcha talabalar:")
# for i in p1.get_all_students():
#     print(i)
# print("------------------------------------------------------------")

# c1.remove_student("Vali")
# print("\n Talaba ochirildi. Yangi ro‘yxat:")
# for i in c1.list_students():
#     print(i)
# print("------------------------------------------------------------")

# p1.remove_course("Web")
# print("\n 1ta kursi o‘chirildi. Yangi kurslar ro‘yxati:")
# for info in p1.list_courses():
#     print(info)
# print("------------------------------------------------------------")





    # Array 34

# s = [5, 3, 7, 2, 6, 1, 4]
# n = len(s)
# mins = []
# for i in range(1, n - 1):
#     if s[i] < s[i - 1] and s[i] < s[i + 1]:
#         mins.append(s[i])
# print("Lokal minimumlar:",mins, "\nKattasi:", max(mins))


# Array 35

# a = [5, 3, 7, 2, 6, 1, 4]
# n = len(a)
# maximum = []
# for i in range(1, n - 1):
#     if a[i] > a[i - 1] and a[i] > a[i + 1]:
#         maximum.append(a[i])
# print("Lokal maksimumlar:", maximum, "\nkichigi:", min(maximum))


# Array 36

# a = [5, 3, 7, 2, 6, 1, 4]
# n = len(a)
# new = []
# for i in range(n):
#     if i == 0 or i == n - 1:
#         new.append(a[i])
#     elif not (a[i] < a[i - 1] and a[i] < a[i + 1]) and not (a[i] > a[i - 1] and a[i] > a[i + 1]):
#         new.append(a[i])
# print("Natija:", max(new))


# Array 37

# a = [1, 3, 5, 2, 4, 6, 7]
# d = 0
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         d += 1
# print("Osuvchilar soni:", d)


# Array 38

# a = [1, 4, 3, 5, 2, 1]
# d = 0
# for i in range(1, len(a)):
#     if a[i] < a[i - 1]:
#         d += 1
# print("Osuvchilar soni:", d)


# Array 39

# a = [1, 3, 5, 2, 4, 6, 7]
# d = 0
# for i in range(1, len(a)):
#     if a[i] > a[i - 1] or a[i] < a[i - 1]:
#         d += 1
# print("monotonlar soni:", d)


# Array 40

# a = [5, 7, 8, 10, 2, 1]
# r = 6
# d = a[0]
# for i in a:
#     if abs(i - r) < abs(d - r):
#         d = i
# print("Eng yaqin element:", d)




# class Salom:
#     nomi = "Lola"
#
#     def __init__(self, name):
#         self.name = name
#
#     def chiq(self):
#         return self.name
#
#     @classmethod
#     def info(cls):
#         return cls.nomi
#
#     @staticmethod
#     def get(a, b):
#         return a ** b
#
# c1 = Salom("Naima")
#
# print(c1.chiq())
# print(c1.info())
# print(c1.get(3, 3))























