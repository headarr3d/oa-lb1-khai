import math  # підключення бібліотеки math

# Завдання 1: Обчислення кількості повних метрів
def task_integer1():
    try:
        l = int(input("Введіть L (см): "))
        if l < 0:
            raise ValueError("L повинно бути додатним цілим числом!")
    except ValueError as e:
        print(f"Помилка: {e}")
    else:
        res = l // 100
        print(f"L = {res} м")

# Завдання 2: Обчислення математичного виразу
def task_float1():
    # Обчислити математичний вираз: y = (log^2(x^2 + cos(37))) / (sin^2(x^2) + √|1 - 2cos(x) - sin^2(x^2)|)
    try:
        x = float(input("Введіть x: "))
    except ValueError:
        print("x має бути числом!")
    else:
        try:
            # Обчислення виразу
            sinx2 = math.sin(x ** 2) ** 2
            numerator = math.log(x ** 2 + math.cos(math.radians(37))) ** 2
            denominator = sinx2 + math.sqrt(abs(1 - 2 * math.cos(x) - sinx2))
            y = numerator / denominator
        except (ValueError, ZeroDivisionError) as e:
            print(f"Помилка обчислення: {e}")
        else:
            print(f"y = {y}")

# Завдання 3: Перевірка істинності висловлювання
def task_boolean1():
    try:
        A = int(input("Введіть A: "))
    except ValueError:
        print("A має бути цілим числом!")
    else:
        res = A > 0
        print(f"A є додатним: {res}")

# Головна функція для запуску
if __name__ == "__main__":
    while True:
        print("\nОберіть завдання:")
        print("1 - Завдання 1 (кількість повних метрів)")
        print("2 - Завдання 2 (математичний вираз)")
        print("3 - Завдання 3 (перевірка позитивності числа)")
        print("0 - Вийти")
        choice = input("Ваш вибір: ")

        if choice == "1":
            task_integer1()
        elif choice == "2":
            task_float1()
        elif choice == "3":
            task_boolean1()
        elif choice == "0":
            print("Вихід із програми.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз!")
