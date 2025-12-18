# Array 58

# a = [1, 2, 3, 4, 5]
# b = []
# for i in range(len(a)):
#     b.append(sum(a[:i+1]))
# print(b)


# Array 59

# a = [1, 2, 3, 4, 5]
# b = []
# for i in range(len(a)):
#     b.append(sum(a[:i+1]) / (i+1))
# print(b)


# Array 60

# a = [1, 2, 3, 4, 5]
# b = []
# for i in range(len(a)):
#     b.append(sum(a[i:]))
# print(b)


# Array 61

# a = [1, 2, 3, 4, 5]
# b = []
# for i in range(len(a)):
#     b.append(sum(a[i:]) / (len(a) - i))
# print(b)


# Array 62

# a = [-2, 3, -1, 5, -7, 8]
# b = []
# c = []
# for x in a:
#     if x >= 0:
#         b.append(x)
#     else:
#         c.append(x)
# print("b =", b)
# print("c =", c)


# Array 63

# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# c = a + b
# print(c)


# Array 64

# a = [3, 1, 2]
# b = [6, 5, 4]
# c = [9, 7, 8]
# d = sorted(a + b + c)
# print(d)


# Array 65

# a = [1, 2, 3, 4, 5]
# k = 2
# for i in range(len(a)):
#     a[i] += a[k]
# print(a)


# Array 66

# a = [1, 2, 3, 4, 6]
# juft = [x for x in a if x % 2 == 0]
# if juft:
#     oxirgi = juft[-1]
#     for i in range(len(a)):
#         if a[i] % 2 == 0:
#             a[i] += oxirgi
# print(a)


# Array 67

# a = [1, 2, 3, 4, 5]
# toq = [x for x in a if x % 2 != 0]
# if toq:
#     oxirgi = toq[-1]
#     for i in range(len(a)):
#         if a[i] % 2 != 0:
#             a[i] += oxirgi
# print(a)


# Array 68

# a = [4, 1, 7, 3, 9]
# mn = a.index(min(a))
# mx = a.index(max(a))
# a[mn], a[mx] = a[mx], a[mn]
# print(a)


# Array 69

# a = [1, 2, 3, 4, 5, 6]
# for i in range(0, len(a), 2):
#     a[i], a[i+1] = a[i+1], a[i]
# print(a)


# Array 70

# a = [1, 2, 3, 4, 5]
# mid = len(a)//2
# for i in range(mid):
#     a[i], a[mid+1+i] = a[mid+1+i], a[i]
# print(a)


# Array 71

# a = [1, 2, 3, 4, 5]
# a.reverse()
# print(a)


# Array 72

# a = [1, 2, 3, 4, 5]
# k = 1
# h = 3
# a[k], a[h] = a[h], a[k]
# print(a)

a = [1, 2, 3, 6, 5, 6, 7]
k = 2
h = 6
for i in a:
    print(i)