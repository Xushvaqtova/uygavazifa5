'''
def nums(num):
    v = 0
    d = 0
    for i in num:
        if i % 2 == 0:
            v += i
        else:
            d += i

    print(f"juft - {v}, toq - {d}")

nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
'''

'''
n = int(input("Iinsert length of list: "))

a = []

for i in range(n):
    x = int(input("Raqam yoz "))
    if x % 2 == 0:
        a.append(x)           
print(a)
'''   

# masala 1
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

juft = [i for i in numbers if i % 2 == 0]
print(juft)
'''


# masala 2
'''
n = 5
a = []
for i in range(n):
    x = input("So'z yoz ")
    a.append(x)           
print(a)
'''

# masala 3
'''
fruits = ['banana', 'apple', 'cherry', 'mango', 'pear']
fruits.sort()
print(fruits)
'''

# masala 4
'''
numbers = [45, 12, 78, 23, 56]

dec = sorted(numbers, reverse = True)
print(dec)
'''

# masala 5
'''
color = ['red', 'blue', 'green', 'yellow', 'blue']
color.remove('blue')
print(color)
'''

# masala 6
'''
x = input("So'z yoz ").split()       
print(len(x))
'''

# masala 7
'''
animals  =['cat', 'dog', 'elephant', 'tger']
print(animals[1])
'''

# masala 8
'''
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:5])
'''


# masala 9
'''
marks = [56, 72, 64, 89, 45]
marks[1] =  100
print(marks)
'''

# masala 10
'''
numbers = [10, 20, 30, 40, 50]

print("Len ", len(numbers))
numbers.append(60)

print("Append ", numbers)

print("Slicing ", numbers[1:3])

dec = sorted(numbers, reverse = True)
print("Sort ", dec)
'''
















































    

