# Считываем первое целое число A
a = int(input())

# Считываем второе целое число B
b = int(input())

# Если A больше B, выводим A
if a > b:
    print(a)

# Если B больше A, выводим B
elif b > a:
    print(b)

# Если числа равны, выводим сообщение
else:
    print("Numbers are equal")


