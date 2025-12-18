# Array 23

# n = [3, 9, 5, 12, 8, 15, 2, 7, 4, 9, 1, 3]
# k = 2
# l = 6
# s = 0
# s += (sum(n[:k]) + sum(n[l:])) / (len(n[:k]) + len(n[l:]))
# print(s)


# Array 26

# s = [2, 5, 8, 7, 2, 5, 8, 4, 9]
# n = -1
# for i in range(len(s) - 1):
#     if s[i] % 2 == s[i + 1] % 2:
#         n = i + 1
#         break
# if n == -1:
#     print(0)
# else:
#     print(f"Soni: {n}")


# Array 27

# s = [2, -5, 9, -7, 2, -5, -8, -4, 9]
# n = -1
# for i in range(len(s) - 1):
#     if s[i]  * s[i + 1] > 0:
#         n = i + 1
#         break
# if n == -1:
#     print(0)
# else:
#     print(f"Soni: {n}")


# Array 28

# s = [1, 2, 3, 4, 5, 7, 6]
# new = []
# for i in s:
#     if i % 2 == 0:
#         new.append(s[i])
# print(min(new))


# Array 29

# s = [1, 2, 3, 4, 5, 7, 6]
# new = []
# for i in s:
#     if i % 2 != 0:
#         new.append(i)
# print(max(new))


# Array 30

# s = [2, 5, 3, 7, 5, 8, 4, 9]
# n = 0
# for i in range(len(s) - 1):
#     if s[i] > s[i + 1]:
#         print(s[i])
#         n += 1
# print(f"Soni: {n}")


# Array 31

# s = [2, 5, 3, 7, 5, 8, 4, 9]
# new = []
# for i in reversed(range(1, len(s))):
#     if s[i] > s[i - 1]:
#         print(s[i], end=" ")
#         new.append(s[i])
# print("\nsoni - ", len(new))


# Array 32

# s = [2, 5, 9, 7, 2, 5, 8, 4, 9]
# n = -1
# for i in range(1, len(s) - 1):
#     if s[i] < s[i - 1] and s[i] < s[i + 1]:
#         n = i
#         break
# if n == -1:
#     print("yoq")
# else:
#     print(f"Soni: {n}")


# Array 33

# s = [2, 5, 9, 7, 2, 5, 8, 4, 9]
# n = -1
# for i in range(1, len(s) - 1):
#     if s[i] > s[i - 1] and s[i] > s[i + 1]:
#         n = i
# if n == -1:
#     print("yoq")
# else:
#     print(f"Soni: {n}")

# a = [5, 3, 7, 2, 6, 1, 4]
# n = len(a)
# turlar = []
#
# for i in range(n):
#     if i == 0 or i == n - 1:
#         turlar.append(a[i])
#     elif not (a[i] < a[i - 1] and a[i] < a[i + 1]) and not (a[i] > a[i - 1] and a[i] > a[i + 1]):
#         turlar.append(a[i])
#
# if turlar:
#     print("Natija:", max(turlar))
# else:
#     print(0)




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
# g1 = Groups("Python N72")
# g1.add_students(s1)
# g1.add_students(s2)
# g1.add_students(s3)
#
# t1 = Teacher("Lola", "Python")
# t1.add_group("Python N72")
#
# print(t1.get_info())
# print("-------------------------")
# print(g1.get_info())
# print("Talabalar soni: ", g1.count_student())
#
# g1.update_student("Noiba", "Nasiba", 22)
# print("-------------------------")
# print(g1.get_info())
# g1.delete_student("Ali")
# print("-------------------------")
# print(g1.get_info())
# print("Talabalar soni: ", g1.count_student())
# print("-------------------------")


















