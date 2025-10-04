a1 = int(input());
a2 = int(input());
b1 = int(input());
b2 = int(input());


color_a = (a1 + a2) % 2;
color_b = (b1 + b2) % 2;

if color_a == color_b:
    print("Yes");
    if color_a == 0:
        print("White");
    else:
        print("Black");
else:
    print("No")

