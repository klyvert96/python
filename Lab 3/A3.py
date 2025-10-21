prev = int(input("Pervious: "))
curr = int(input("Current: "))

if curr >= prev:
    used = curr - prev
else:
    used = (10000 - prev) + curr

if used <= 300:
    cost = 21
elif used <= 600:
    cost = 21 + (used - 300) * 0.06
elif used <= 800:
    cost = 21 + 300 * 0.06 + (used - 600) * 0.04
else:
    cost = 21 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025

avg_price = cost / used

print(f"{'Previous':<12}{'Current':<10}{'Used':<12}{'To Pay':<10}{'Avg. price/m^3':<15}")
print(f"{prev:<12}{curr:<10}{used:<12}{cost:<10.2f}{avg_price:<15.2f}")
