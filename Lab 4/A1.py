import random
import time

def ask_int(prompt):
    """Спрашивает целое число — повторяет, пока не будет введено корректно."""
    while True:
        val = input(prompt)
        if val.lstrip('-').isdigit():
            return int(val)
        else:
            print("Пожалуйста, введите целое число!")

def multiplication_trainer():
    N = ask_int("Введите количество примеров: ")

    correct = 0
    total_time = 0.0

    for i in range(1, N + 1):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        answer = a * b

        print(f"Вопрос {i}/{N}")

        start = time.time()

        while True:
            user_input = input(f"{a} × {b} = ")
            if user_input.lstrip('-').isdigit():
                user_answer = int(user_input)
                break
            else:
                print("Пожалуйста, введите целое число!")

        end = time.time()
        elapsed = end - start
        total_time += elapsed

        if user_answer == answer:
            correct += 1
            print(f"Верно! (Время: {elapsed:.1f} сек)")
        else:
            print(f"Неверно! Правильно: {answer} (Время: {elapsed:.1f} сек)")

    # --- вывод статистики ---
    print("=" * 50)
    print("СТАТИСТИКА:")
    print("=" * 50)
    print(f"Общее время: {total_time:.1f} секунд")
    print(f"Среднее время на вопрос: {total_time / N:.1f} сек")
    print(f"Правильных ответов: {correct}/{N}")
    print(f"Процент правильных: {correct / N * 100:.1f}%")


multiplication_trainer()

