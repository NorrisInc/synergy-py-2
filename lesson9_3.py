import io

def main():
    print("Урок 9.3 - Множества: поиск дубликатов")
    print("=" * 50)
    try:
        nums = list(map(int, input("Введите числа через пробел: ").split()))
        seen = set()
        for x in nums:
            print(f"Встречалось ли число {x} в множестве ранее: ")
            if x in seen:
                print("  YES")
            else:
                print("  NO")
                seen.add(x)

    except ValueError:
        print("Ошибка: нужно вводить только числа")
    input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
