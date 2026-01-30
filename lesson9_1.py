import io

def main():
    print("Урок 9.1 - Множества: разные числа")
    print("=" * 50)
    
    try:
        flag = True
        while flag:
            n = int(input("Указажите количество чисел: "))
            if (1 <= n <= 100000):
                flag = False
                continue
            print("Ввод в первую строку должен соответсвовать условию: 1 ≤ N ≤ 100000")
        nums = list(map(int, input(f"Введите через пробел {n} чисел: ").split()))
        nums = nums[:n]  # отсекаю лишние элементы
        print(f"Число разных чисел среди данных: {len(set(nums))}")
        
        input("Нажмите Enter для продолжения...")
        
    except ValueError:
        print("Ошибка: введите целое число!")
        input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
