T = int(input());
h = T // 3600;
m = (T % 3600) // 60;
s = T % 60;
if s < 10 and m < 10:
    print(f"{h}:0{m}:0{s}")
elif s < 10:
    print(f"{h}:{m}:0{s}")
elif m < 10:
    print(f"{h}:0{m}:{s}")
else:
    print(f"{h}:{m}:{s}")
