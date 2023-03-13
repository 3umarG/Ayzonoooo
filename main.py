import math as ms

str = "Omar Gomaa"

print(str * 3)
print(str[0:4] * 2)
print(str.split())
print(str.split("a"))
print(str.splitlines())
print(str.partition('m'))
print(str.find("ama"))
print(str.replace("a", "e"))
print(str.count("aa"))
print(str.upper())
print(str.capitalize())
print(str.swapcase())
print(str.title())
a = True
b = False
print(a, b)

# List

l = [1, 2, 5, 6, "Omar", True, [2, 4, 8]]
print(l[6][1])
name = "Omar"
nl = list(name)
print(nl)
l.remove(2)
print(l)

a = [1, 2, 3, 4]
a.pop()
print(a)
a.pop(1)
print(a)

# Tuple
t = 1, 2, 3, 5
print(t)
print(type(t))
ls = list(t)
print(ls)

# Set
set = {n for n in range(10)}
set2 = {n for n in range(12)}
print(set.union(set2))

# Dictionary
dic = {n: n ** 2 for n in range(5)}
print(dic)
print(16 in dic.values())
print(16 in dic)


dic2 = dic.copy()
print(dic2)
dic2[5] = 25
print(dic2)

