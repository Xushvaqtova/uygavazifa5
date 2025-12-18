# Masala 1

# nums = [1,2,3,4,5,6,7,8,9,10]
# toq = [x for x in nums if x % 2 != 0]
# print(toq)


# Masala 2

# num = [x*x for x in range(1, 11)]
# print(num)


# Masala 3

# soz = ["salom", "dunyo", "pythonista", "kod", "informatika", "ai"]
# uzun = [i for i in soz if len(i) > 5]
# print(uzun)


# Masala 4

# num = [10, -3, 0, 5, -1]
# son = ["musbat" if x > 0 else ("manfiy" if x < 0 else "nol") for x in num]
# print(son)



# Masala 5

# s = "salom"
# asc = {i: ord(i) for i in s}
# print(asc)



# Masala 6

# num = {i: i**3 for i in range(1,6)}
# print(num)



# Masala 7

# nums = [1,2,2,3,4,4,5,6,6]
# juft = {x for x in nums if x % 2 == 0}
# print(juft)



# Masala 8

# soz = ["hello","to","kod","python","test","data"]
# sett = {i for i in soz if len(i) % 2 == 0}
# print(sett)


# Masala 9

# nums = [3, -2, 0, 5, -7]
# yechim = {x: (x*x if x > 0 else 0) for x in nums}
# print(yechim)


# Masala 10

# text = "salom dunyo salom"
# sana = {i: text.count(i) for i in set(text)}
# print(sana)


# Masala 1

# d = {1: 50, 2: 10, 3: 30, 4: 20}
# sotli = dict(sorted(d.items(), key=lambda x: x[1]))
# print(sotli)


# Masala 2

# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# dct = {**dic1, **dic2, **dic3}
# print(dct)


# Masala 3


# kvadrat = {i: i**2 for i in range(1, 15)}
# print(kvadrat)


# Masala 4

# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
# sum = sum(d.values())
# print(sum)


# Masala 5

# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
# maxv = max(d.values())
# print(maxv)


# Masala 6

# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
# minv = min(d.values())
# print(minv)


# Masala 7

# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# s = {k: d1.get(k, 0) + d2.get(k, 0) for k in set(d1) | set(d2)}
# print(s)


# Masala 8

# lst = [
#     {"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#     {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# unikv = {list(d.values())[0] for d in lst}
# print(unikv)


# Masala 9

# soz = "assalom"
# harflar = {}
# for harf in soz:
#     if harf in harflar:
#         harflar[harf] += 1
#     else:
#         harflar[harf] = 1
# for harf, soni in harflar.items():
#     print(harf, soni, "ta")


# Masala 10

# soz = "mexanizasiyalashtirilganmi"
# natija = {}
# for harf in soz:
#     if harf in natija:
#         natija[harf] += 1
#     else:
#         natija[harf] = 1
# maxharf = max(natija, key=natija.get)
# print("Harf - ",maxharf, "soni - ", natija[maxharf] )


# Masala 11

# def lotincha(text):
#     harflar = {
#         "а":"a", "б":"b", "в":"v", "г":"g", "д":"d", "е":"e", "ё":"yo",
#         "ж":"j", "з":"z", "и":"i", "й":"y", "к":"k", "л":"l", "м":"m",
#         "н":"n", "о":"o", "п":"p", "р":"r", "с":"s", "т":"t", "у":"u",
#         "ф":"f", "х":"x", "ц":"ts", "ч":"ch", "ш":"sh", "щ":"sh", "ъ":"ʼ",
#         "ы":"y", "ь":"", "э":"e", "ю":"yu", "я":"ya", "қ":"q", "ғ":"g‘",
#         "ҳ":"h", "ў":"o‘", "ң":"ng", "ў":"o‘", "ж":"j", "ч":"ch", "ш":"sh",
#         "ь":"", "э":"e", "ю":"yu", "я":"ya", "ё":"yo", "ў":"o‘", "ғ":"g‘", "қ":"q", "ҳ":"h", "з":"z"}
#     return ''.join([harflar.get(i, i) for i in text.lower()])
# print(lotincha("ўзбекча салом бериш керак менга"))


# Masala 12

# def krilcha(text):
#     harflar = {
#         "a":"а", "b":"б", "d":"д", "e":"е", "f":"ф", "g":"г", "h":"ҳ",
#         "i":"и", "j":"ж", "k":"к", "l":"л", "m":"м", "n":"н", "o":"о",
#         "p":"п", "q":"қ", "r":"р", "s":"с", "t":"т", "u":"у", "v":"в",
#         "x":"х", "y":"й", "z":"з", "ch":"ч", "sh":"ш", "ng":"нг",
#         "yo":"ё", "ya":"я", "yu":"ю", "o‘":"ў", "g‘":"ғ"}
#     for i, j in sorted(harflar.items(), key=lambda x: -len(x[0])):
#         text = text.replace(i, j)
#     return text
# print(krilcha("o‘zbekcha salom berishingiz kerak hammaga"))



# Masala 1

# try:
#     son = int(input("Son kiriting "))
#     natija = son / 2
#     print(natija)
# except ZeroDivisionError:
#     print("Bo‘linish mumkin emas")
# except Exception:
#     print("Xatolik yuz berdi")
# finally:
#     print("Dastur tugadi")


# Masala 2

# try:
#     f = open("mashq1.txt", "r")
#     qator = f.readline().strip()
#     son = int(qator)
#     print(son / 100)
# except FileNotFoundError:
#     print("Fayl topilmadi")
# except ValueError:
#     print("Malumot notogri")
# finally:
#     print("tugadi")


# Masala 3

# try:
#     son = int(input("Son kiriting "))
#     s = son // 10
#     print("Qoldiq:", s)
# except ZeroDivisionError:
#     print("0 ga bolinish mumkin emas")
# except Exception:
#     print("Xatolik yuz berdi")
# else:
#     print("Hisoblash muvaffaqiyatli")


# Masala 4

# try:
#     a = int(input("a ni kiriting: "))
#     b = int(input("b ni kiriting: "))
#     natija = a / b
#     print(float(natija))
# except ValueError:
#     print("Faqat raqam kiriting")
# except ZeroDivisionError:
#     print("Bo‘linishda 0 ga bo‘lish xatosi")
# except Exception:
#     print("xatolik yuz berdi")
# finally:
#     print("peratsiya tugadi")


# Masala 5
# lst = [25, 0, "a"]
# def hisobla(lst):
#     try:
#         s = lst.pop(2)
#         print(s / 100)
#     except IndexError:
#         print("Bunday index yoq")
#     except ZeroDivisionError:
#         print("0 ga bolinmaydi")
#     except (TypeError, ValueError):
#         print("Qiymat son emas")
#     finally:
#         lst.insert(2, s)
#         print("Ro‘yxat tiklandi:", lst)
# hisobla(lst)


# Masala 6

# try:
#     with open("numbers.txt", "r") as f:
#         sonlar = f.read().split()
#         sonlar = [int(x) for x in sonlar]
#         print("Yigindi:", sum(sonlar))
# except FileNotFoundError:
#     print("numbers.txt topilmadi")
# except ValueError:
#     print("Faylda son bolmagan malumot bor")


# Masala 7

# with open("output.txt", "w") as f:
#     for i in range(1, 21):
#         f.write(str(i) + "\n")


# Masala 8

# matn = input("Matn kiriting: ")
# with open("log.txt", "a") as f:
#     f.write(matn + "\n")


# Masala 9

# with open("words.txt", "r") as f:
#     for i in f:
#         print(i.strip().upper())


# Masala 10

# with open("data.txt", "r") as f:
#     son = f.read().replace(",", " ")
#     i = [int(x) for x in son.split()]
#     print("Eng katta son:", max(i))


# Masala 12

# with open("students.txt", "r") as f, open("passed.txt", "w") as out:
#     for qator in f:
#         ism, baho = qator.strip().split()
#         if int(baho) > 70:
#             out.write(ism + " " + baho + "\n")


# Masala 13

# with open("source.txt", "r") as src, open("copy.txt", "w") as dst:
#     for qator in src:
#         dst.write(qator)



















































