'''
def power_234(x):
    print(x ** 2)
    print(x ** 3)
    print(x ** 4)

power_234(int(input("Son kiriting ")))    
'''
from itertools import count

# def mean(a, b, c, d):
#     ab = (a+b)/2
#     ac = (a+c)/2
#     ad = (a+d)/2
#     print(ab)
#     print(ac)
#     print(ad)
#
# mean(2, 3, 4, 5)


# # masala 61
#
# data = (1, 2, 3, 2, 4, 2, 5, 6, 2, 7)
# d = []
# s = 0
# for i in data:
#     if i == 2:
#         d.append(s)
#     s += 1
# print(d)


# masala 62

# words = ["salom","dunyo","python","dasturlash"]
# s = []
# for i in words:
#         s.append(len(i))
# print(s)


# masala 63

# t = (5,10,15,20,25,30,35,40)
# t1 = ()
# t2 = list(t1)
# for i in t:
#     if i % 3 == 0:
#         t2.append(i)
# t1 = tuple(t2)
# print(t1)


# masala 64

# numbers = [3,1,4,1,5,9,2,6,5]
# numbers.sort()
# num = []
# for i in numbers:
#     if i not in num:
#         num.append(i)
# print(num)


# qoshimcha 1
'''
nums = [1, 2, 3, 2, 4, 1, 5]

def unique(nums):
    s = 0
    for i in nums:
        if nums.count(i) == 1:
            s += i
    print(s)
unique(nums)
'''


# qoshimcha 3
'''
nums = [0, 1, 0, 3, 12, 0, 5]
def nol_count(nums):
    yangi = []
    nol = []
    for i in nums:
        if i == 0:
            nol.append(i)
        else:
            yangi.append(i)
    natija = yangi + nol
    print(natija) 
nol_count(nums)
'''


# qoshimcha 4
'''
nums = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]
def dublicat_mal(nums):
    num = []
    for i in nums:
        if nums.count(i) == 2 and i not in num:
            num.append(i)
    print(num)
dublicat_mal(nums)
'''

# qoshimcha 5
'''
nums = [1, 2, 3, 2, 1, 4, 3, 8]
def unikal_mal(nums):
    uni = []
    for num in nums:
        if nums.count(num) == 1:
            uni.append(num)
    if len(uni) > 0:
        print(uni[-1])
    else:
        print(None)
unikal_mal(nums)
'''


































