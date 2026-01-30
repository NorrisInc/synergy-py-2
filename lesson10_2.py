import io

def main():
    print("Урок 10.2 - Словари: ключ и значение в степени ключа")
    print("=" * 50)
    try:
        my_dict = {}
        rng = int(input("Введите размер словаря: ").strip())
        for x in range(rng):
            inp = int(input(f"Введите значение ключа № {x + 1}: ").strip())
            my_dict[inp] = inp**inp
        print(f"Вот твой словарь, где значение ключа возвеведно в степень ключа: {my_dict}")
        
    except ValueError:
        print("Ошибка: нужно вводить числа")
    input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
