x1 = int(input());
y1 = int(input());
x2 = int(input());
y2 = int(input());


def quarter(x, y):
    if x > 0 and y > 0:
        return "I"
    elif x < 0 and y > 0:
        return "II"
    elif x < 0 and y < 0:
        return "III"
    elif x > 0 and y < 0:
        return "IV"

q1 = quarter(x1, y1);
q2 = quarter(x2, y2);

if q1 == q2:
    print(f"Yes, {q1}")
else:
    print("No")
