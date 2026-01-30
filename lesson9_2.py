import io

def main():
    print("Урок 9.2 - Множества: два списка")
    try:
        a = list(map(int, input("Укажите числа через пробел для первого списка: ").split()))
        b = list(map(int, input("Укажите числа через пробел для второго списка: ").split()))
        print(f"Количество чисел в двух списках: {len(set(a) & set(b))}")
    except ValueError:
        print("Ошибка: нужно вводить числа")
    input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
