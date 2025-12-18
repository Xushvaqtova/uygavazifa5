'''
number = [1, 2, 3, 4, 5, 6, 8]
print(len(number))


mlist = list(('olma', 'behi'))
print(mlist)


number = [1, 2, 3, 4, 5, 6, 8]
print(number[3])


number = [1, 2, 3, 4, 5, 6, 8]
number[1] = 100
print(number)


number = [1, 2, 3, 4, 5, 6, 8]
number[1:4] = ['besh', 123]
print(number)


number = [1, 2, 3, 4, 5, 6, 8]
number.append(345)
print(number)


number = [1, 2, 3, 4, 5, 6, 8]
number.insert(5, 'Toqqiz')
print(number)


number = [1, 2, 3, 4, 5, 6, 8]
week = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba']
#number.extend(week)
week.extend(number)
#print(number)
print(week)


week = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba']
week.remove('Seshanba')
print(week)


week = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba']
week.pop()
print(week)


week = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba']
week.pop(1)
print(week)


week = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba']
del week[0]
print(week)


week = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba']
week.clear()
print(week)


week = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba']
week.sort()
print(week)


week = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba']
week.reverse()
print(week)


week = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba']
wek = [5, 6]
week = wek
print(week)


week = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba']
wek = [5, 6]
week = wek.copy()
print(week)


week = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba']
print(week.count('Seshanba'))


week = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba']
print(week.index('Seshanba'))


week = ('Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba')
print(len(week))


week = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba']
week[1] = 'Juma'
print(week)
print(week[2:4])
print(week[3:])
print(week[:5])
print(week[-2])
print(week[-3:-1])


week = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba']
del week
print(week)


week = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba']
print(week.count('Seshanba'))


week = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba']
print(week.index('Seshanba'))


a = [1, 1, 3, 4, 4, 5, 6, 7]
b = [0, 1, 2, 3, 4, 4, 5, 7, 8]
a.extend(b)
print(sum(a)/len(a))


a = [1, 3, 5, 7, 9, 10]
b = [2, 4, 6, 8]
a.pop()
a.extend(b)
print(a)
'''


a = [1, 4, 3, 9]
b = []
for i in a:
    b.append('RM' + (str(i)))
print(b)




































































































