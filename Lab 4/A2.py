# --------------------------------------
# Функция 1: Прямоугольник n × m
# --------------------------------------
def draw_rectangle(n, m, sym):
    print("\nПрямоугольник:")
    for i in range(n):
        for j in range(m):
            print(sym, end="")
        print()


# --------------------------------------
# Функция 2: Правый треугольник
# --------------------------------------
def draw_triangle(n, sym):
    print("\nПравый треугольник:")
    for i in range(1, n + 1):
        for j in range(i):
            print(sym, end="")
        print()


# --------------------------------------
# Функция 3: Рамка n × m
# --------------------------------------
def draw_frame(n, m, sym):
    print("\nРамка:")
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                print(sym, end="")
            else:
                print(" ", end="")
        print()


# --------------------------------------
# Главное меню программы
# --------------------------------------
def main():
    while True:
        print("\n=== МЕНЮ ===")
        print("1 — Прямоугольник")
        print("2 — Правый треугольник")
        print("3 — Рамка")
        print("0 — Выход")

        choice = input("Выберите фигуру: ")

        if choice == "1":
            n = int(input("Введите высоту (n): "))
            m = int(input("Введите ширину (m): "))
            sym = input("Введите символ для рисования: ")
            draw_rectangle(n, m, sym)

        elif choice == "2":
            n = int(input("Введите число строк: "))
            sym = input("Введите символ для рисования: ")
            draw_triangle(n, sym)

        elif choice == "3":
            n = int(input("Введите высоту (n): "))
            m = int(input("Введите ширину (m): "))
            sym = input("Введите символ для рисования: ")
            draw_frame(n, m, sym)

        elif choice == "0":
            print("Выход из программы...")
            break

        else:
            print("Ошибка! Выберите пункт 0–3.")


# Запуск программы
main()

