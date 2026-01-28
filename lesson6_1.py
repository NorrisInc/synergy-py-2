import io

def main():
    print("Урок 6.1 - Циклы: поиск нулевых значений")
    print("=" * 50)
    
    try:
        n = int(input("Введите количество целых чисел: ").strip())
        zeros = 0
        for i in range(n):
            if int(input(f"Input # {(i + 1)}: ").strip()) == 0:
                zeros = zeros + 1
        print(f"Нулевых значений: {zeros}")

    except ValueError:
        print("Ошибка ввода числа. Введите число")
    input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
