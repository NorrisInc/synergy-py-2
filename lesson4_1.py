import io

def main():
    print("Урок 4.1 - Площадь и периметр")
    try:
        a = float(input("Введите длину первой стороны: "))
        b = float(input("Введите длину второй стороны: "))

        if a <= 0 or b <= 0:
            print("Ошибка: стороны должны быть положительными числами!")
            return

        area = a * b
        perimeter = 2 * (a + b)

        print("РЕЗУЛЬТАТЫ:")
        print(f"Сторона a = {a}")
        print(f"Сторона b = {b}")
        print(f"Площадь S = {a} × {b} = {area}")
        print(f"Периметр P = 2 × ({a} + {b}) = {perimeter}")
        
        # Если целые числа - выводим без дробной части
        if a.is_integer() and b.is_integer():
            print(f"\n(В целых числах: S = {int(area)}, P = {int(perimeter)})")
        
    except ValueError:
        print("Ошибка: введите корректное число!")
    input("Нажмите Enter для продолжения...")
    
if __name__ == "__main__":
    main()
