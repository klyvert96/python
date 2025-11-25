def get_input_sequence():
    """Функция ввода и проверки корректности строки"""
    while True:
        seq = input("Введите последовательность пакетов (0 и 1, длина ≥ 5): ")
        if len(seq) < 5:
            print("Ошибка: длина строки должна быть не менее 5.")
            continue
        if not all(c in "01" for c in seq):
            print("Ошибка: строка должна содержать только символы 0 и 1.")
            continue
        return seq

def analyze_sequence(seq):
    total_packets = len(seq)
    lost_packets = seq.count('0')

    # Находим длину самой длинной последовательности потерянных пакетов
    max_lost_streak = 0
    current_streak = 0
    for c in seq:
        if c == '0':
            current_streak += 1
            if current_streak > max_lost_streak:
                max_lost_streak = current_streak
        else:
            current_streak = 0

    loss_percent = (lost_packets / total_packets) * 100

    # Оценка качества связи
    if loss_percent <= 1:
        quality = "Отличное качество"
    elif loss_percent <= 5:
        quality = "Хорошее качество"
    elif loss_percent <= 10:
        quality = "Удовлетворительное качество"
    elif loss_percent <= 20:
        quality = "Плохое качество"
    else:
        quality = "Критическое состояние сети"

    return total_packets, lost_packets, max_lost_streak, loss_percent, quality

def main():
    seq = get_input_sequence()
    total, lost, max_streak, percent, quality = analyze_sequence(seq)

    print("\n===== СТАТИСТИКА СЕТИ =====")
    print(f"Общее количество пакетов: {total}")
    print(f"Количество потерянных пакетов: {lost}")
    print(f"Длина самой длинной последовательности потерь: {max_streak}")
    print(f"Процент потерь: {percent:.2f}%")
    print(f"Оценка качества связи: {quality}")

if __name__ == "__main__":
    main()

