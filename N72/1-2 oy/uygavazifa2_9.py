# Masala 1


a = ('behi', 'olma', 12, 34)
b = list(a)
b.append(input("Nimadir yozing: "))
a = tuple(b)
print(a)


# Masala 2

# a = ('behi', 'olma', 12, 34)
# b = list(a)
# s = input("Nimadir yozing: ") # tupleni ichidagi narsani yozing
# if s.isdigit():
#     s = int(s)
# b.remove(s)
# a = tuple(b)
# print(a)


# Masala 3

# a = ('behi', 'olma', 12, 34)
# b = list(a)
# b.reverse()
# a = tuple(b)
# print(a)


# Masala 4

# a = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# res = []
# for i in a:
#     tem = list(i)
#     tem[-1] = 100
#     tem = tuple(tem)
#     res.append(tem)
# print(res)


# Masala 5

# a = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# b = list(a)
# b.remove(())
# b.remove(())
# print(b)


# Masala 6

# a = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if float(a[i][1]) < float(a[j][1]):
#             a[i], a[j] = a[j], a[i]
# print(a)



# Masala 7

# a = {'olma', 'anor', 'behi', 'malina'}
# b = {'behi', 'gilos', 'qulupnay', 'olma'}
# a.difference_update(b)
# print(a)


# Masala 8

# a = {1, 2, 3, 4, 5}
# b = {2, 4, 6, 8, 3}
# new = a.intersection(b)
# print(min(new))


# Masala 9

# a = {"olma", "anor", "behi", "gilos"}
# s = input("Element kiriting: ")
# if s in a:                              # A setni ichida bor elementni yozsangiz bor chiqadi yo'qsa yoq chiqadi
#     print("Bor")
# else:
#     print("Yo‘q")


# Dict 1

# dostlar = {
#         "Bekzod" : { "age" :  23, "city"  :  "buxoro"},
#         "Shahriz" : { "age" :  20, "city"  :  "Toshkent"},
#         "Asila" : { "age" :  10, "city"  :  "Samarqand"} }
# print( len(dostlar))


# Dict 2

# bozor = {
#             1 :  "olma",
#             2  :  "anor",
#             3 :  "gilos",
#             4  :  "Qulupnay",
#             5 :  "malina",
#             6  :  "nok"}
# print( len(bozor))


# Dict 3

# talaba = {
#      't1' : {'name' : 'Bob', "age" :  25},
#      't2' : {'name' : 'Kim', "age" :  23},
#      't3' : {'name' : 'Sam', "age" :  20}}
# for i in talaba.values():
#     print(i["age"] )


# Dict 4

# mashina = {
#      'm1' : {'model' : 'M5', "color" :  "Qora", "year" :  2025},
#      'm2' : {'model' : 'k5', "color" :  "Yashil", "year" :  2020},
#      'm3' : {'model' : 'm3', "color" :  "Kok"},
#      'm4' : {'model' : 'k7', "color" :  "Sariq"}}
# for i in mashina.values():
#     if 'year' in i:
#         print(i["year"] )
#     else:
#         print(None)


# Dict 5

# meva = {
#             1 :  "olma",
#             2 :  "anor",
#             3 :  "gilos",
#             4 :  "Qulupnay",
#             5 :  "malina",
#             6 :  "nok"}
# for i in meva.keys():
#     print(i)


# Dict 6

# talaba = {
#      't1' : {'name' : 'Bob', "age" :  25},
#      't2' : {'name' : 'Kim', "age" :  23},
#      't3' : {'name' : 'Sam', "age" :  20}}
# for i in talaba.keys():
#     print(i)


# Dict 7

# dostlar = {
#         "d1" : {'name' : 'Bob', "age" :  23},
#         "d2" : {'name' : 'Sara', "age" :  20},
#         "d3" : {'name' : 'Olga', "age" :  10} }
# for i in dostlar.values():
#     print(i['name'], i['age'])


# Dict 8

# meva = {
#         1 : {'name' : "olma", 'price' : 12000},
#         2 : {'name' : "anor", 'price' : 15000},
#         3 : {'name' : "gilos", 'price' : 20000},
#         4 : {'name' : "Qulupnay", 'price' : 13000},
#         5 : {'name' : "malina", 'price' : 25000},
#         6 : {'name' : "nok", 'price' : 10000}}
# for i in meva.values():
#     print(i['name'], i['price'])


# Dict 9

# book = {
#         "k1" : {'title' : 'marketing qurboni', "author" :  "Nick jonas"},
#         "k2" : {'title' : 'Aleksa', "author" :  "Morgan Ray"},
#         "k3" : {'title' : 'Qalbim', "author" :  "shehriban"} }
# for i in book.values():
#     print(i.values())


# Dict 10

# telefon = {
#         1 : {'brand' : "Iphone", 'price' : 120000},
#         2 : {'brand' : "SAMSUNG", 'price' : 1500000},
#         3 : {'brand' : "XIAOMI", 'price' : 200000},
#         4 : {'brand' : "OPPO", 'price' : 130000}}
# for i,j in telefon.items():
#     print(i, j)



# Dict 11

# dost = {
#         'name' : 'Bob',
#         "age" :  23,
#         "city"  :  "buxoro" }
# dost.update({'city' : "Eron"})
# print(dost)


# Dict 12

# mashina = {
#         'brand' : 'BMW',
#         "model" :  "m5",
#         "color"  :  "qora" }
# mashina.update({'color' : "qizil"})
# print(mashina)


# Dict 13

# talaba = {
#         'name':'Bob',
#         "age" : 23,
#         "city": "buxoro" }
# talaba['course'] =  "python"
# print(talaba)


# Dict 14

# meva = {
#         'name' : "olma",
#         'price' : 12000}
# meva.update({'price' : 400000})
# print(meva)


# Dict 15

# book = {
#         'title' : 'marketing qurboni',
#         "author" :  "Nick jonas"}
# book['pages'] = 200
# print(book)


# Dict 16

# mashina = {
#         'model' : 'M5',
#         "color" :  "Qora",
#         "year" :  2025}
# mashina['engine'] = 'm4'
# print(mashina)


# Dict 17

# talaba = {
#         'name':'Bob',
#         "age" : 23,
#         "city": "buxoro" }
# talaba.pop('age')
# print(talaba)


# Dict 18

# telefon = {
#         'brand' : "Iphone",
#         'model' : "XS",
#         'price' : 120000}
# telefon.pop('price')
# print(telefon)


# Dict 19

# dostlar = {
#         "Bekzod" : { "age" :  23, "city"  :  "buxoro"},
#         "Shahriz" : { "age" :  20, "city"  :  "Toshkent"},
#         "Asila" : { "age" :  10, "city"  :  "Samarqand"} }
# dostlar.popitem()
# print(dostlar)


# Dict 20

# mashina = {
#         'model' : 'M5',
#         "color" :  "Qora",
#         "year" :  2025}
# print(mashina.popitem())


# Dict 21

# talaba = {
#         'name':'Bob',
#         "age" : 23,
#         "city": "buxoro" }
# talaba.pop('name')
# print(talaba)


# Dict 22

# mashina = {
#         'model' : 'M5',
#         "color" :  "Qora",
#         "year" :  2025}
# del mashina
# print(mashina)


# Dict 23

# telefon = {
#         'brand' : "Iphone",
#         'model' : "XS",
#         'price' : 120000}
# telefon.clear()
# print(telefon)


# Dict 24

# bozor = {
#             1 :  "olma",
#             2  :  "anor",
#             3 :  "gilos",
#             4  :  "Qulupnay",
#             5 :  "malina",
#             6  :  "nok"}
# bozor.clear()
# print(bozor)


# Dict 25

# talaba = {
#         'name':'Bob',
#         "age" : 23,
#         "city": "buxoro" }
# talaba1 = talaba.copy()
# print(talaba1)


# Dict 26

# mashina = {
#         'model' : 'M5',
#         "color" :  "Qora",
#         "year" :  2025}
# mashina1 = dict(mashina)
# mashina1['year'] = 2020
# print(mashina1)


# Dict 27

# talaba = {
#         'name':'Bob',
#         "age" : 23,
#         "city": "buxoro" }
# talaba1 = dict(talaba)
# print(talaba1)


# Dict 28

# mashina = {
#         'model' : 'M5',
#         "color" :  "Qora",
#         "year" :  2025}
# print(mashina)


# Dict 29

# talaba = {
#         'name':'Bob',
#         "age" : 23,
#         "city": "buxoro" }
# print(talaba.keys())  # tepada for bilan ishlab chiqarganligim uchun shu usulda chiqardim


# Dict 30

# mashina = {
#         'model' : 'M5',
#         "color" :  "Qora",
#         "year" :  2025}
# print(mashina.values()) # tepada for bilan ishlab chiqarganligim uchun shu usulda chiqardim


# Dict 31

# talaba = {
#         'name':'Bob',
#         "age" : 23,
#         "city": "buxoro" }
# # print(talaba.keys(), talaba.values())  # 2ta yol bilan chiqarsa boladi
# for i, j in talaba.items():
#     print(i, j)


# Dict 32

# book = {
#         'title' : 'marketing qurboni',
#         "author" :  "Nick jonas",
#         'pages' : 200 }
# for i, j in book.items():
#     print(i, ":", j)


# Qoshimcha 1

# a = {'a': 10, 'b': 3, 'c': 7}
# print(min(a.values()))


# Qoshimcha 2

# a = {'banana': 5, 'apple': 3, 'cherry': 7}
# s = ""
# for i in a.keys():
#     if len(i) > len(s):
#         s = i
# print(s)


# Qoshimcha 3

# talabalar = {
#     "Ali": [4, 5, 3],
#     "Vali": [5, 5, 4],
#     "Hasan": [3, 2, 4] }
# new = {}
# for i, j in talabalar.items():
#     s = sum(j) / len(j)
#     new[i] = s
# print(new)

# Qoshimcha 4

# data = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 1, "f": 2}
# val = list(data.values())
# mx = 0
# kop = 0
# for i in val:
#     count = val.count(i)
#     if count > mx:
#         mx = count
#         kop = i
# print(kop)


# Qoshimcha 5

# d = {"a": 1, "b": 2, "c": 1}
# res = {}
# for i, j in d.items():
#     if j not in res:
#         res[j] = [i]
#     else:
#         res[j].append(i)
# print(res)











