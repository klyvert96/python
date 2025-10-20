prev = int(input())
curr = int(input())

# вычисляем расход
if curr >= prev:
    used = curr - prev
else:
    used = (10000 - prev) + curr

# вычисляем оплату
if used <= 300:
    cost = 21
elif used <= 600:
    cost = 21 + (used - 300) * 0.06
elif used <= 800:
    cost = 21 + 300 * 0.06 + (used - 600) * 0.04
else:
    cost = 21 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025

avg_price = cost / used

# Заголовок с выравниванием по ширине
print(f"{'Предыдущее':<12}{'Текущее':<10}{'Использовано':<14}{'К оплате':<10}{'Ср. цена m^3':<12}")
# Данные с выравниванием
print(f"{prev:<12}{curr:<10}{used:<14}{cost:<10.2f}{avg_price:<12.2f}")

