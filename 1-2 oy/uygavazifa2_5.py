# masala 1
'''
son = [10, 20, 30, 40, 50]
print(len(son))
'''

# masala 2
'''
meva = ['olma', 'anor', 'banan', 'gilos']
print(len(meva))
'''

# masala 3
'''
meva = ('olma', 'nok', 'behi')
mevalist = list(meva)
print(mevalist)
'''


# masala 4
'''
soz = 'salom'
sozlist = list(soz)
print(sozlist)
'''

# masala 5
'''
rang = ['qizil', 'yashil', 'sariq', 'kok']
print(rang[2])
'''

# masala 6
'''
son = [12, 45, 67, 89]
print(son[-1])
'''

# masala 7
'''
week = ['Dushanba', 'Juma', 'Shanba']
week[1] = 'Seshanba'
print(week)
'''

# masala 8
'''
meva = ['olma', 'anor', 'banan']
meva[-1] = 'nok'
print(meva)
'''

# masala 9
'''
week = ['Dushanba', 'Juma', 'Shanba']
week[1:3] = 'Seshanba','Chorshanba'
print(week)
'''

# masala 10
'''
son = [1, 2, 3, 4, 5]
son[2:4] = 8, 9
print(son)
'''

# masala 11
'''
son = [1, 2, 3]
son.append(4)
print(son)
'''

# masala 12
'''
meva = ['olma', 'nok']
meva.append('behi')
print(meva)
'''

# masala 13
'''
meva = ['olma', 'anor', 'uzum']
meva.insert(2, 'banan')
print(meva)
'''

# masala 14
'''
son = [10, 20, 40]
son.insert(2, 30)
print(son)
'''

# masala 15
'''
a = [1, 2, 3]
b = [5, 6]
a.extend(b)
print(a)
'''

# masala 16
'''
ism = ['ali', 'vali']
yosh = [23, 45]
ism.extend(yosh)
print(ism)
'''

# masala 17
'''
meva = ['olma', 'anor', 'uzum']
del meva[1]
print(meva)
'''

# masala 18
'''
son = [1, 2, 3, 2, 4]
del son[1]
print(son)
'''

# masala 19
'''
alfa = ['a', 'b', 'c']
alfa.pop()
print(alfa)
'''

# masala 20
'''
son = [10, 20, 30, 40]
son.pop(1)
print(son)
'''

# masala 21
'''
son = [1, 2, 3, 4]
#del son[2] #ikalasidan biri ochirish deganiga ikkalasini ham yozdim.
son.pop(2)
print(son)
'''

# masala 22
'''
meva = ['olma', 'anor', 'banan']
del meva
print(meva)
'''

# masala 23
'''
son = [1, 2, 3, 4, 5]
son.clear()
print(son)
'''

# masala 24
'''
alfa = ['a', 'b', 'c']
alfa.clear()
print(alfa)
'''

# masala 25
'''
son = [5, 3, 8, 1]
son.sort()
print(son)
'''

# masala 26
'''
meva = ['banan', 'olma', 'anor']
meva.sort(reverse = True)
print(meva)
'''

# masala 27
'''
son = [1, 2, 3, 4]
son.reverse()
print(son)
'''

# masala 28
'''
alfa = ['a', 'b', 'c']
alfa.reverse()
print(alfa)
'''

# masala 29
'''
son = [1, 2, 3]
son1 = []
son1 = son.copy()
print(son1)
'''

# masala 30
'''
meva = ['olma', 'anor']
meva1 = []
meva1 = meva.copy()
print(meva1)
'''

# masala 31
'''
meva = ['olma', 'anor', 'olma', 'banan']
print(meva.count('olma'))
'''

# masala 32
'''
son = [1, 2, 3, 2, 2, 4]
print(son.count(2))
'''

# masala 33
'''
meva = ['olma', 'anor', 'banan']
print(meva.index('banan'))
'''

# masala 34
'''
son = [10, 20, 30, 40]
print(son.index(30))
'''

# masala 35
'''
son = (10, 20, 30, 40)
print(len(son))
'''

# masala 36
'''
meva = ('olma', 'anor', 'nok')
print(len(meva))
'''

# masala 37
'''
city = ('Buxoro', 'Parij', 'London')
print(city[1])
'''

# masala 38
'''
son = (5, 10, 15, 20, 25)
print(son[-1])
'''

# masala 39
'''
meva = ('Olma', 'Anor')
meva1 = list(meva)
meva1[1] = 'Banan'
print(meva1)
#meva  = tuple(meva1) # bu shartda tuple bolsin yoki list korinishda tusin deyilmagan shu uchun ikki xil qolda ishladim
#print(meva)
'''

# masala 40
'''
son = (1, 2, 3)
son1 = list(son)
son1.append(4)
son  = tuple(son1)
print(son)
'''

# masala 41
'''
mytuple = (1, 2, 3)
del mytuple
print(mytuple)
'''

# masala 42
'''
alfa = ['a', 'b', 'c']
del alfa
print(alfa)
'''

# masala 43
'''
meva = ('olma', 'anor', 'olma', 'nok')
for i in meva:
    print(i)
'''

# masala 44
'''
son = (10, 20, 30)
for i in son:
    print(i)
'''

# masala 45
'''
meva = ('olma', 'anor', 'olma', 'nok')
print(meva.count('olma'))
'''

# masala 46
'''
son = (1, 2, 3, 2, 4, 2)
print(son.count(2))
'''

# masala 47
'''
meva = ('olma', 'anor', 'banan')
print(meva.index('banan'))
'''

# masala 48
'''
son = (5, 10, 15, 20)
print(son.index(15))
'''

# masala 49
'''
son = [5, 3, 8, 1]
print(min(son))
'''

# masala 50
'''
son = (12, 45, 7, 33)
print(min(son))
'''

# masala 51
'''
son = [10, 50, 30, 20]
print(max(son))
'''

# masala 52
'''
son = (1, 100,  23, 45)
print(max(son))
'''

# masala 53
'''
son = [1, 2, 3, 4, 5]
print(sum(son))
'''

# masala 54
'''
son = (10, 20, 30)
print(sum(son))
'''

# masala 55
'''
son = [4, 7, 2, 9, 12, 5]
print("Oraqsidagi farq ", max(son) - min(son))
'''

# masala 56
'''
city = ("Toshkent","Buxoro","Xiva","Samarqand","Andijon")
print(city[2:5])
'''

# masala 57
'''
soz = ["python","java","c++","go","python","go"]
new = []
for i in soz:
    if i in new:
        pass
    else:
        new.append(i)
print(len(new))
'''

# masala 58
'''
num = (10, 20, 30, 40, 50)
print('Yigindi ', sum(num), )
print('Ortacha qiymat ', sum(num)/len(num))
'''

# masala 59
'''
fruits = ["olma","anor","banan"]
fruits.append('uzum')
fruits.insert(0, 'shaftoli')
print(fruits)
'''

# masala 60
'''
nums = [12, 7, 5, 64, 14, 9, 33]
num = []
for i in nums:
    if i % 2 == 0:
        num.append(i)
print(num)
'''

# masala 61
'''
data = (1, 2, 3, 2, 4, 2, 5, 6, 2, 7)
d = []
s = 0
for i in data:                            
    if i == 2:
        d.append(s)
    s += 1    
print(d)
'''

# masala 62
'''
words = ["salom","dunyo","python","dasturlash"]
s = []
for i in words:                                   
        s.append(len(i))
print(s)
'''

# masala 63
'''
t = (5,10,15,20,25,30,35,40)
t1 = ()
t2 = list(t1)
for i in t:
    if i % 3 == 0:
        t2.append(i)
t1 = tuple(t2)        
print(t1)
'''

# masala 64
'''
numbers = [3,1,4,1,5,9,2,6,5]
numbers.sort()
num = []
for i in numbers:
    if i not in num:
        num.append(i)
print(num)
'''

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







