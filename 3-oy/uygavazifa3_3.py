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

# s = "abcdjf"
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