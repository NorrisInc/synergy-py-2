import io

def main():
    print("Урок 6.3 - Циклы: отрезок и четные числа")
    print("=" * 50)
    
    try:
        A = int(input("Введите число A: "))
        B = int(input("Введите число B: "))
        
        if A > B:
            print("Ошибка: должно быть A <= B")
            input("Нажмите Enter для продолжения...")
            return
        
        print(f"\nОтрезок: [{A}, {B}]")
        print(f"Длина отрезка: {B - A + 1} чисел")
        
        # Собираем четные числа
        even_numbers = []
        
        for num in range(A, B + 1):
            if num % 2 == 0:
                even_numbers.append(num)
        
        print(f"\nЧетные числа на отрезке:")
        
        if even_numbers:
            # Выводим через пробел
            print(", ".join(map(str, even_numbers)))
            
            # Дополнительная информация
            print(f"\nСтатистика:")
            print(f"   Всего четных чисел: {len(even_numbers)}")
            print(f"   Всего нечетных чисел: {(B - A + 1) - len(even_numbers)}")
            print(f"   Процент четных: {len(even_numbers)/(B - A + 1)*100:.1f}%")
            
            # Первое и последнее четное
            print(f"   Первое четное: {even_numbers[0]}")
            print(f"   Последнее четное: {even_numbers[-1]}")
            
            if len(even_numbers) > 1:
                print(f"   Шаг между четными: {even_numbers[1] - even_numbers[0]}")
        else:
            print("На отрезке нет четных чисел!")
        
        input("Нажмите Enter для продолжения...")
        return even_numbers
        
    except ValueError:
        print("Ошибка: введите целые числа!")
    input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
