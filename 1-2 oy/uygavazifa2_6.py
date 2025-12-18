#List 1

# lst = ["apple", "banana", "cherry", "kiwi"]
# for i in lst:
#     if "a" in i:
#         print(i)


# List 2

# lst = ["apple", "banana", "cherry", "kiwi"]
# yangi = []
# for i in lst:
#     if "a" not in i:
#         yangi.append(i)
# print(yangi)


# list 3

# nums = [2, 4, 6, 8]
# s = 0
# for i in nums:
#     s += i
# print(s)


# list 4

# nums = [2, 3, 4, 6]
# s = 1
# for i in nums:
#     s *= i
# print(s)


# list 5

# lst = [1, 2, 2, 3, 4, 4, 5]
# yangi = []
# for i in lst:
#     if i not in yangi:
#         yangi.append(i)
# print(yangi)


# list 6

# a = [1, 2, 3]
# b = [4, 5, 2]
# teng = False
# for x in a:
#     if x in b:
#         teng = True
# print(teng)


# list 7

# nums = [1, 2, 3, 4, 5, 6]
# yangi = []
# for i in nums:
#     if i % 2 != 0:
#         yangi.append(i)
# print(yangi)


# list 8

# lst = ["olma", "banan", "nok"]
# print(lst[1])


# list 9

# nums = [3, 8, 1, 10, 5]
# mx = nums[0]
# for i in nums:
#     if i > mx:
#         mx = i
# print(mx)


# list 10

# nums = [3, 8, 1, 10, 5]
# mn = nums[0]
# for i in nums:
#     if i < mn:
#         mn = i
# print(mn)


# list 11

# nums = [3, 8, 1, 10, 5]
# mx = nums[0]
# for i in nums:
#     if i > mx:
#         mx = i
# mx2 = nums[0]
# for i in nums:
#     if i > mx2 and i < mx:
#         mx2 = i
# print(mx2)


# list 12

# nums = [3, 8, 1, 10, 5]
# mn = nums[0]
# for i in nums:
#     if i < mn:
#         mn = i
# mn2 = nums[0]
# for i in nums:
#     if i < mn2 and i > mn:
#         mn2 = i
# print(mn2)


# list 13

# son = [1, 2, 3, 4, 5, 6, 7]
# yangi = []
# for i in son:
#     yangi.append(i*i)
# print(yangi)


# list 14

# lst = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# lst[2][1][2].append("h")
# lst[2][1][2].append("i")
# lst[2][1][2].append("j")
# print(lst)


# list 15

# matn = "salom python assalom dunyo"
# sozlar = matn.split()
# s = 5
# for i in sozlar:
#     if len(i) == s:
#         print(i)


# list 16

# a = "salom python assalom python salom dunyo"
# sozlar = a.split()
# for i in sozlar:
#     soni = 0
#     for y in sozlar:
#         if i == y:
#             soni += 1
#     print(i, soni, "ta")


# list 17

# nums = [5, 2, 8, 1, 3]
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if nums[i] < nums[j]:
#             nums[i], nums[j] = nums[j], nums[i]
# print(nums)


# list 18

# mylist = ['a','b','c']
# yangi = []
# for i in range(len(mylist)):
#     for j in range(i+1, len(mylist)):
#         yangi.append(mylist[i]+mylist[j])
# print(yangi)


# list 19

# a = 0
# b = 1                   #nn
# for i in range(13):
#     a, b = b, a+b
# print(a)


# list 20

# matn = "salom bugun python darsi juda qiziq"
# sozlar = matn.split()
# mx = sozlar[0]
# for i in sozlar:
#     if len(i) > len(mx):
#         mx = i
# print(mx)


# list 21

# nums = [1, 2, 3, 2, 4, 1, 5]
# def unique(nums):
#     s = 0
#     for i in nums:
#         if nums.count(i) == 1:
#             s += i
#     print(s)
# unique(nums)


# list 22

# nums = [4, 1, 2, 2, 3, 2]
# unique_list = []
# count_list = []
# for i in nums:
#     if i not in unique_list:
#         unique_list.append(i)
# for i in unique_list:
#     count_list.append(nums.count(i))
# max_count = max(count_list)
# for i in unique_list:
#     if nums.count(i) == max_count:
#         print(i, "soni", max_count, "marta chiqadi")


# list 23

# nums = [0, 1, 0, 3, 12, 0, 5]
# def nol_count(nums):
#     yangi = []
#     nol = []
#     for i in nums:
#         if i == 0:
#             nol.append(i)
#         else:
#             yangi.append(i)
#     natija = yangi + nol
#     print(natija)
# nol_count(nums)


# list 24

# nums = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]
# def dublicat_mal(nums):
#     num = []
#     for i in nums:
#         if nums.count(i) == 2 and i not in num:
#             num.append(i)
#     print(num)
# dublicat_mal(nums)


# list 25

# nums = [1, 2, 3, 2, 1, 4, 3, 8]
# def unikal_mal(nums):
#     uni = []
#     for num in nums:
#         if nums.count(num) == 1:
#             uni.append(num)
#     if len(uni) > 0:
#         print(uni[-1])
#     else:
#         print(None)
# unikal_mal(nums)


# Set 1

# myset = {1, 2, 3, 4, 5}
# print(len(myset))


# Set 2

# myset = {"olma", "anor"}
# myset.add("uzum")
# print(myset)


# Set 3

# myset = {"a", "b"}
# myset2 = {"c", "d"}
# myset.update(myset2)
# print(myset)


# Set 4

# myset = {"olma", "anor", "uzum"}
# myset.remove("anor")
# print(myset)


# Set 5

# myset = {"olma", "anor", "uzum"}
# myset.discard("shaftoli")  # yoq bolsa ham xato bermaydi
# print(myset)


# Set 6

# myset = {"a", "b", "c", "d"}
# myset.pop()
# print(myset)


# Set 7

# myset = {1, 2, 3, 4}
# myset.clear()
# print(myset)


# Set 8

# myset = {"a", "b", "c"}
# del myset
# print(myset)


# Set 9

# myset1 = {"olma", "anor"}
# myset2 = {"uzum", "anor"}
# yangi = myset1.union(myset2)
# print(yangi)


# Set 10

# myset1 = {"a", "b", "c"}
# myset2 = {"b", "c", "d"}
# new = myset1.intersection(myset2)
# print(new)


# Set 11

# myset1 = {"olma", "anor", "gilos"}
# myset2 = {"anor", "o‘rik"}
# myset1.symmetric_difference_update(myset2)
# print(myset1)


# Set 12

# myset1 = {"a", "b", "c"}
# myset2 = {"b", "c", "d"}
# yangi = myset1.symmetric_difference(myset2)
# print(yangi)



# Qoshimcha 1

# nums = [1, 2, 3, 4, 5, 6, 2, 8, 4, 10, 11]
# result = set()
# for i in nums:
#     if i % 2 == 0:
#         result.add(i)
# print(result)



# Qoshimcha 2

# words = ["level", "world", "madam", "python", "refer", "hello"]
# result = set()
# for i in words:
#     if i == i[::-1]:
#         result.add(i)
# print(result)


# Qoshimcha 3

# def kesishma(lst1, lst2):
#     return set(lst1).intersection(lst2)
# print(kesishma([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))


# Qoshimcha 4

# def sozlar_toplami(ac):
#     result = set()
#     for i in ac:
#         result.update(i.split())
#     return result
# print(sozlar_toplami(["I love Python", "Python is great", "I love coding"]))


# Qoshimcha 5

# nums = ["+998901234567", "1234567", "+998931112233"]
# result = []
# for i in nums:
#     if i.startswith("+998") and len(i) == 13:
#         result.append(i)
# print(result)







