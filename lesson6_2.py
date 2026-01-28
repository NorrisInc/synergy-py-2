import io

def main():
    print("Урок 6.2 - Циклы: натуральные делители")
    print("=" * 50)
    try:
        X = int(input("Введите натуральное число X: "))
        
        if X <= 0:
            print("Число должно быть натуральным (больше 0)!")
            input("Нажмите Enter для продолжения...")
            return
        
        if X > 2e9:
            print("Число слишком большое для этого метода!")
            input("Нажмите Enter для продолжения...")
            return
        
        divisors = []
        count = 0
        
        for i in range(1, X + 1):
            if X % i == 0:
                divisors.append(i)
                count += 1
        
        print(f"\nРЕЗУЛЬТАТЫ ДЛЯ ЧИСЛА {X}:")
        print(f"   Всего делителей: {count}")
        print(f"   Делители: {divisors}")
        
        if count == 2:
            print("   Это простое число!")
        elif count % 2 == 0:
            print("   Четное количество делителей")
        else:
            print("   Нечетное количество делителей")
        
        input("Нажмите Enter для продолжения...")
        return count
        
    except ValueError:
        print("Ошибка: введите целое число!")
    input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
