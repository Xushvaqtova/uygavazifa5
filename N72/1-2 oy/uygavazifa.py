import csv
# Masala 1

# with open('data.txt', 'r') as file:
#     oqi = file.read()
# yangi = ""
# soz = ""
# for i in oqi:
#     if i != " ":
#         soz = i + soz
#     else:
#         yangi += soz + " "
#         soz = ""
# yangi += soz
# with open("natija.txt", "w")as f:
#     f.write(yangi)


# Masala 2

# with open('natija.txt', 'r') as file:
#     sozlar = file.read().split()
# for i in range(len(sozlar)):
#     for j in range(i+1, len(sozlar)):
#         if sozlar[i] > sozlar[j]:
#             sozlar[i], sozlar[j] = sozlar[j], sozlar[i]
# print(" ".join(sozlar))


# Masala 3

# with open("natija.txt", 'r') as file:
#     sozlar = file.read().split()
# uzun = sozlar[0]
# for i in sozlar:
#     if len(i) > len(uzun):
#         uzun = i
# with open("log.txt", 'w') as f:
#     f.write(uzun)


# Masala 4

# with open("natija.txt", 'r') as file:
#     sozlar = file.read().split()
# uzun = sozlar[0]
# for i in sozlar:
#     if len(i) < len(uzun):
#         uzun = i
# with open("log.txt", 'w') as f:
#     f.write(uzun)


# Masala 5

# with open('natija.txt', 'r') as file:
#     sozlar = file.read().split()
# for i in range(len(sozlar)):
#     for j in range(i+1, len(sozlar)):
#         if len(sozlar[i]) < len(sozlar[j]):
#             sozlar[i], sozlar[j] = sozlar[j], sozlar[i]
# print(" ".join(sozlar))


# Masala 7

# with open("data.txt", "w") as f:
#     for i in range(1, 11):
#         for j in range(1, 11):
#             f.write(f"{i} * {j} = {i * j}\t")
#         f.write("\n")


# Masala 8

# a = int(input("Son kiriting "))
# with open("data.txt", 'r') as f:
#     qator = f.readlines()
# for i in qator[-a:]:
#     print(i.strip())

# Masala 9

# with open("natija.txt", 'r') as f:
#     sozlar = f.read()
# soz = sozlar.split()
# print(len(soz))




# Masala  1 csv

# data = [10, 20, 30, 40, 50]
#
# with open("data.csv", 'w', newline="") as f:
#     yoz = csv.writer(f)
#     yoz.writerow(data)
#
# with open("data.csv", 'r') as f:
#     red = csv.reader(f)
#     for i in red:
#         s = [int(x) for x in i]
# print(sum(s))



# Masala 2

# students = [ {"name": "Ali", "age": 20},
#              {"name": "Vali", "age": 22},
#              {"name": "Hasan", "age": 21}]
#
# with open("data.csv", "w", newline='') as file:
#     yoz = csv.DictWriter(file)
#     yoz.writeheader('name', 'age')
#     yoz.writerows(students)
#
#
# with open('data.csv', 'r') as file:
#     oqi = csv.DictReader(file)
#     maks = max(oqi, key=lambda x: int(x["age"]))
# print(maks["name"], maks["age"])


# Masala 3

# n = int(input("Nechta son kiritasiz "))
# sonlar = []
# for i in range(n):
#     son = int(input(f"{i+1}-sonni kiriting "))
#     sonlar.append(son)
#
#
# with open("data.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(sonlar)
#
# with open("data.csv", "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         sonlar = [int(x) for x in row]
#
# juft = 0
# for s in sonlar:
#     if s % 2 == 0:
#         juft += 1
# print(juft)


# Masala 4

# matn = "assalomu alaykum"
# ch = {}
#
# for harf in matn:
#     ch[harf] = ch.get(harf, 0) + 1
#
# with open("data.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["harf", "soni"])
#     for i, j in ch.items():
#         writer.writerow([i, j])
#
# with open("data.csv", "r") as f:
#     reader = csv.DictReader(f)
#     maks = max(reader, key=lambda x: int(x["soni"]))
# print( maks["harf"], "harfi", maks["soni"], "marta chiqdi")



# Masala 5

# grades = [
#     {"name": "Ali", "grade": 85},
#     {"name": "Vali", "grade": 72},
#     {"name": "Hasan", "grade": 90} ]
#
# with open("grades.csv", "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=["name", "grade"])
#     writer.writeheader()
#     writer.writerows(grades)
#
# with open("grades.csv", "r") as f:
#     reader = csv.DictReader(f)
#     baholar = [int(row["grade"]) for row in reader]
#
# print("Ortacha", sum(baholar) / len(baholar))


# Masala 6

# with open("kvadrat.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["son", "kvadrat"])
#     for i in range(1, 21):
#         writer.writerow([i, i*i])
#
# with open("kvadrat.csv", "r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         if int(row["kvadrat"]) > 200:
#             print(row["son"], row["kvadrat"])


# Masala 7

# rates = [
#     {"nomi": "USD", "qiymat": 12600},
#     {"nomi": "EUR", "qiymat": 13800},
#     {"nomi": "RUB", "qiymat": 150} ]
#
# with open("rates.csv", "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=["nomi", "qiymat"])
#     writer.writeheader()
#     writer.writerows(rates)
#
# with open("rates.csv", "r") as f:
#     reader = csv.DictReader(f)
#     maks = max(reader, key=lambda x: int(x["qiymat"]))
# print(maks["nomi"], maks["qiymat"])


# Masala 8

# ismlar = []
# for i in range(5):
#     ism = input(f"{i+1}-ismni kiriting: ")
#     ismlar.append({"ism": ism, "uzunlik": len(ism)})
#
# with open("ismlar.csv", "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=["ism", "uzunlik"])
#     writer.writeheader()
#     writer.writerows(ismlar)
#
# with open("ismlar.csv", "r") as f:
#     reader = csv.DictReader(f)
#     maks = max(reader, key=lambda x: int(x["uzunlik"]))
# print(maks["ism"], maks["uzunlik"])


# Masala 9

# fruits = [
#     {"name": "Olma", "price": 12000},
#     {"name": "Banan", "price": 15000},
#     {"name": "Uzum", "price": 10000} ]
#
# with open("fruits.csv", "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=["name", "price"])
#     writer.writeheader()
#     writer.writerows(fruits)
#
# with open("fruits.csv", "r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         if int(row["price"]) > 12000:
#             print(row["name"], row["price"])


# Masala 10

# results = [
#     {"name": "Ali", "ball": 75},
#     {"name": "Vali", "ball": 55},
#     {"name": "Hasan", "ball": 95}]
# 
# with open("results.csv", "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=["name", "ball"])
#     writer.writeheader()
#     writer.writerows(results)
# 
# with open("results.csv", "r") as f:
#     reader = csv.DictReader(f)
#     for i in reader:
#         if int(i["ball"]) < 60:
#             print(i["name"], i["ball"], " yiqildi")
#         else:
#             print(i["name"], i["ball"], " o‘tdi")
