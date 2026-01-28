import io

def main():
    print("Урок 5.1 - Анализ числа")
    print("=" * 50)
    
    try:
        # Ввод числа
        num = int(input("Введите целое число: "))
        
        print(f"\nАнализируем число: {num}")
        print("-" * 30)
        
        # Проверяем особый случай - ноль
        if num == 0:
            print("Результат: нулевое число")
            input("Нажмите Enter для продолжения...")
            return
        
        # Определяем знак
        if num > 0:
            sign = "положительное"
        else:
            sign = "отрицательное"
        
        # Определяем четность
        if num % 2 == 0:
            parity = "четное"
        else:
            parity = "нечетное"
        
        # Формируем результат
        result = f"{sign} {parity} число"
        
        print(f"Знак: {sign}")
        print(f"Четность: {parity}")
        print(f"\nРезультат: {result}")
        
    except ValueError:
        print("Ошибка: введите целое число!")
    input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
