# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных
x, y, z = int(input()), int(input()), int(input())
b, n, m = abs(x), abs(y), abs(z)
b = b is x
n = n is y
m = m is z
print(b+n+m)
