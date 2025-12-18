# class Student:
#     def __init__(self, name, age, otm, course):
#         self.name = name
#         self.age = age
#         self.otm = otm
#         self.course = course
#
#     def get_info(self):
#         return f"Talaba malumoti:\n Ismi: {self.name}\n Yoshi: {self.age}\n Instituti: {self.otm}\n Kursi: {self.course}"
#
# c1 = Student('Ali', 20, "Milliy universiteti", 2)
# c2 = Student('Lola', 21, "TATU", 4)
#
# class Oqituvchi(Student):
#     def  __init__(self, name, age, otm, course, maktab, dsoat):
#         super().__init__(name, age, otm, course)
#         self.dsoat = dsoat
#         self.maktab = maktab
#
#     def get_info(self):
#         return f"Talaba malumoti:\n Ismi: {self.name}\n Yoshi: {self.age}\n Instituti: {self.otm}\n Kursi: {self.course}\n Maktab: {self.maktab}\n DArs soati {self.dsoat}"
#
# o1 = Oqituvchi('Madina', 20, "Milliy universiteti", 3, "35=maktab", '22 soat')
# print(o1.get_info())
import stat
from idlelib.replace import replace
from os.path import split

# s = "salom men keldim nss"
# soz = s.split()
# s1 = min(len(i) for i in soz)
# short = [i for i in soz if len(i) == s1][-1]
# print(short)


 # class Cars:
#     def __init__(self, make, name, model):
#         self.make = make               #public
#         self._name = name              #protected
#         self.__model = model           #private
#
#     def get_cars_info_public(self):
#         return f"\n Mashina malumotlari:\n Zavod nomi: {self.make}\n "
#
#     def _get_cars_info_protected(self):
#         return f"\n Mashina malumotlari:\n Mashina nomi: {self._name}\n "
#
#     def __get_cars_info_private(self):
#         return f"\n Mashina malumotlari:\n  Modeli: {self.__model}"
#
# class Oil_cars(Cars):
#      def __init__(self, make, name, model, color):
#         Cars.__init__(self, make, name, model)
#         self.color = color
#
#     def get_oil_cars_info(self):
#         return f"Gaz mashina malumotlari:\n Rangi: {self.color}, {self.get_cars_info_public()}\n {self._get_cars_info_protected()}"
#
# c1 = Oil_cars("Bayerische Motoren Werke AG", "BMW", "M5", "green")
# print(c1.get_oil_cars_info())



#
# class Electro_cars(Cars):
#     def __init__(self, name, model,  yomkast):
#         Cars.__init__(self, name, model)
#         self.yomk = yomkast
#
#     def get_electro_cars_info(self):
#         return f"Elektr mashina malumotlari:\n Maksimal zaryadi: {self.yomk}"
#
#
# class Gibrid(Oil_cars, Electro_cars):
#     def __init__(self, name, model, color, yomkast):
#         Oil_cars.__init__(self, name, model, color)
#         Electro_cars.__init__(self, name, model, yomkast)
#
#         self.color = color
#
#     def get_oil_cars_info(self):
#         return f"Gaz mashina malumotlari:\n Rangi: {self.color}"




# string 1

# s = "a"
# print(ord(s))


# string 2

# s = "x"
# i = ord(s)
# if 32 < i < 126:
#     print(i)


# string 3

# s = "x"
# i = ord(s)
# print(chr(i+1), chr(i-1))


# string 4

# s = int(5)
# for j in range(s):
#     print(chr(ord("A")+j))


# string 5

# s = int(5)
# for i in range(s-1, -1, -1):
#     print(chr(ord("a") + i))

# string 6

# s = "0"
# if s.isdigit():
#     print("digit")
# else:
#     print("lotin")


# string 7

# s = "salom"
# f = s[0]
# l = s[-1]
# print(ord(f), ord(l))


# string 8

# n = 6
# belgi = "A"
# print(belgi*n)


# string 9

# s = "saalm"
# d = "nma"
# print(s+d)

# string 10

# s = "salom"
# print(s[::-1])


# string 11

# s = "salom"
# print(" ".join(s))


# string 12

# s = "Salom"
# n = 3
# print(("*"* n ).join(s))


# string 13

# s = "salom 12, meninh1 ismi34m nim234 a"
# soz = s.split()
# d = 0
# for i in soz:
#     for j in i:
#         if j.isdigit():
#             d += 1
# print(d)


# string 14

# s = "Ana MEN senGA nIm a DegAN eDiM"
# d = 0
# soz = s.split()
# for i in soz:
#     for j in i:
#         if j.isupper():
#             d += 1
# print(d)


# string 16

# s = "Ana MEN senGA nIm a DegAN eDiM"
# print(s.lower())


# string 17

# s = "Ana MEN senGA nIm a DegAN eDiM"
# print(s.lower())


# string 18

# s = "Ana MEN senGA nIm a DegAN eDiM"
# print(s.swapcase())


# s = "Ana MEN senGA nIm a DegAN eDiM"
# res = ""
# for i in s:
#     if "A" <= i <= "Z":
#         res += chr(ord(i) + 32)
#     elif "a" <= i <= "z":
#         res += chr(ord(i) - 32)
#     else:
#         res += i
# print(res)


# string 20

# s = "123 12 23"
# print(s)

# string 21

# s = "123 45 67"
# print(s[::-1])

# string 22

# s = "12 3 56 7"
# soz = s.split()
# d = sum(int(i)for i in soz)
# print(d)


# string 23

# s = input()
# print(eval(s))


# string 24



# string 25





 # String 26

# son = 5
# satr = "asalmisan"
# if len(satr) > son:
#     d = satr[-son:]
# elif len(satr) < son:
#     d = "." * (son - len(satr)) + satr
# else:
#     d = satr
# print(d)


# String 27

# s1 = "assalomu"
# s2 = "alaykum"
# n1 = 3
# n2 = 3
# s = s1[:n1]
# d = s2[-n2:]
# new = s + d
# print(new)


# String 28

# c = "c"
# satr = 'crocadile'
# d = ""
# for i in satr:
#     if i == c:
#         d += c*2
#     else:
#         d += i
# print(d)


# String 29

# c = "c"
# satr = "crocadile"
# s2 = "w"
# d = ""
# for i in satr:
#     if i == c:
#         d += s2 + c
#     else:
#         d += i
# print(d)


# String 30

# c = "c"
# s1 = "crocad"
# s2 = "w"
# d = ""
# for i in s1:
#     if i  == c:
#         d += c + s2
#     else:
#         d += i
# print(d)


# String 31


# s1 = "assalom"
# s2 = "sa"
# d = True
# if s2 in s1:
#     d = True
# else:
#     d = False
# print(d)


# String 32

# s1 = "assalom"
# s2 = "sa"
# c = s1.count(s2)
# print(c)


# String 33

# s1 = "meni seni sen qildim sen esa sen"
# s2 = "sen"
# d = s1.replace(s2, "", 1)
# print(d)


# String 34

# s1 = "meni seni sen qildim sen esa sen"
# s2 = "sen"
# soz = s1.split()
# d = ""
# for i in reversed(range(len(soz))):
#     if soz[i] == s2:
#         soz.pop(i)
#         break
# d = " ".join(soz)
# print(d)

# s1 = "meni seni sen qildim sen esa sen"
# s2 = "sen"
# start = s1.rfind(s2)
# end = start + len(s2)
# res = s1[:start] + s1[end:]
# print(res)


# String 35

# s1 = "meni seni sen qildim sen esa sen"
# s2 = "sen"
# d = s1.replace(s2, "")
# print(d)


# String 36

# s1 = "meni seni sen qildim sen esa sen"
# s2 = "sen"
# s3 = "ww"
# d = s1.replace(s2, s3, 1)
# print(d)


# String 37

# s1 = "meni seni sen qildim sen esa sen"
# s2 = "sen"
# s3 = "ww"
# soz = s1.split()
# d = ""
# for i in reversed(range(len(soz))):
#     if soz[i] == s2:
#         soz[i] = s3
#         break
# d = " ".join(soz)
# print(d)


# String 38

# s1 = "meni seni sen qildim sen esa sen"
# s2 = "sen"
# s3 = "ww"
# res = s1.replace(s2, s3)
# print(res)


# String 39

# s = "ab de do"
# soz = s.split()
# if len(soz) == 3:
#     print(soz[1])
# else:
#     print("")


# String 40

# s = "ab de do"
# first = s.find(" ")
# last = s.rfind(" ")
# d = ""
# if first == last:
#     d += ""
# else:
#     d = s[first+1:last]
# print(d)


# String 41

# s = "salom qani alik qani bb sd s"
# soz = s.split()
# print(len(soz))


# String 42

# s = "TURT TORT DEDI MAM DED MOROZ DEMI"
# d = 0
# soz = s.split()
# for i in soz:
#     if i[0] == i[-1]:
#         d += 1
# print(d)


# String 43

# s = "TAURT TORT DEDI MAAM DEsAD MORAAAAAOZ DEMI"
# d = 0
# soz = s.split()
# for i in soz:
#     if "A" in i:
#         d += 1
# print(d)


# String 44

# s = "TURT TORT DEADAAI AMAMA ADED MAOARAOZ DEMI"
# d = 0
# soz = s.split()
# for i in soz:
#     if i.count("A")  == 3:
#         d += 1
# print(d)


# String 45

# s = "salom sen meni se"
# soz = s.split()
# print(min(len(i) for i in soz))


# String 46

# s = "salom sen meni se"
# soz = s.split()
# print(max(len(i) for i in soz))


# String 47

# s = "salom de menga"
# soz = s.split()
# d = "-".join(soz)
# print(d)


# String 50

# s = "  salom de      menga        axmoq"
# soz = s.split()
# print(" ".join(soz[::-1]))


# String 51

# s = "salom berdik   amoq     yamoq  nima"
# soz = s.split()
# print(" ".join(sorted(soz)))


# String 52

# s = "salom berdik   amoq     yamoq  nima"
# soz = s.split()
# d = [i.capitalize() for i in soz]
# print(" ".join(d))


# String 53

# s = "seni! menga$ beganmi* & ^ $ %"
# d = 0
# for i in s:
#     if not i.isalnum() and not i.isspace():
#         d += 1
# print(d)


# String 54

# s = "SAloM Mening KAsbim Yoq"
# d = 0
# for i in s:
#     if i.isupper():
#         d += 1
# print(d)


# String 55

# s = "salom mening ismim nimaligini bilmayman"
# soz = s.split()
# uzun = soz[0]
# for i in soz:
#     if len(i) > len(uzun):
#         uzun = i
# print(uzun)


# String 56

# s = "menin ismim nimaligini bilmayman nsomi"
# soz = s.split()
# min = min(len(i) for i in soz)
# sh = [i for i in soz if len(i) == min][-1]
# print(sh)


# s = "salom men keldim nss"
# soz = s.split()
# uzun = soz[0]
# for i in reversed(soz):
#     if len(i) < len(uzun):
#         uzun = i
# print(uzun)


# String 57

# s = "salom    mening       ismu=im         nima"
# print(" ".join(s.split()))


# String 58

# s = r"D:\Qudrat_c++\books\My_book.exe"
# soz = s.split("\\")[-1]
# d = soz.split(".")[0]
# print(d)


# String 59

# s = r"D:\Qudrat_c++\books\My_book.exe"
# soz = s.split("\\")[-1]
# d = soz.split(".")[1]
# print(soz)


# String 60

# s = r"D:\Qudrat_c++\books\My_book.exe"
# soz = s.split("\\")[1]
# print(soz)


# String 61

# s = r"D:\Qudrat_c++\books\My_book.exe"
# soz = s.split("\\")[2]
# print(soz)


# String 62

# s = "sa lom de"
# new = ""
# for i in s:
#     if i.isalpha():
#         if i == "z":
#             new += "a"
#         elif i == "Z":
#             new += "A"
#         else:
#             new += chr(ord(i) + 1)
#     else:
#         new += i
# print(new)


# String 63

# s = "abcd"
# new = ""
# son = 5
# for i in s:
#     if i.isalpha():
#         if i == "z":
#             new += "a"
#         elif i == "Z":
#             new += "A"
#         else:
#             new += chr(ord(i) + son)
#     else:
#         new += i
# print(new)


# String 64

# s = "fghi"
# new = ""
# son = 5
# for i in s:
#     if i.isalpha():
#         if i == "z":
#             new += "a"
#         elif i == "Z":
#             new += "A"
#         else:
#             new += chr(ord(i) - son)
#     else:
#         new += i
# print(new)

# String 65

# s = "ucnqo"
# first = "s"
# k = ord(s[0]) - ord(first)
# new = ""
# for i in s:
#     new += chr(ord(i) - k)
# print(new)


# String 66

# s = "Programma"
# juft = ""
# toq = ""
# for i in range(len(s)):
#     if i % 2 == 0:
#         juft += s[i]
#     else:
#         toq += s[i]
# new = juft + toq[::-1]
# print(new)


# String 67

# s = "Pormamagr"
# yarm = (len(s) + 1) // 2
# juft = s[:yarm]
# toq = s[yarm:][::-1]
# res = "".join(i+j for i, j in zip(juft, toq))
# if len(juft) > len(toq):
#     res += juft[-1]
# print(res)


# String 68

# s = "abcdjf"
# d = None
# for i in s:
#     if i.isalpha() and i.islower():
#         if d is None:
#             d = i
#         elif i < d:
#             print(i)
#             break
#         d = i
# else:
#     print(0)

# String 69



# String 70



