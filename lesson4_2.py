import io

def main():
    print("Урок 4.2 - Площадь и периметр")
    print("=" * 50)
    
    while True:
        try:
            num = input("Введите пятизначное целое число: ").strip()
            
            if not num.isdigit():
                print("Ошибка: введите только цифры!")
                continue
                
            if len(num) != 5:
                print("Ошибка: число должно быть пятизначным!")
                continue
            
            # Преобразуем в целое
            num_int = int(num)
            break
            
        except ValueError:
            print("Ошибка ввода!")
    
    # Получаем отдельные цифры
    # Преобразуем число в строку для доступа к цифрам
    digits = [int(d) for d in str(num_int)]
    
    # Разряды (слева направо)
    ten_thousands = digits[0]  # десятки тысяч
    thousands = digits[1]      # тысячи
    hundreds = digits[2]       # сотни
    tens = digits[3]           # десятки
    ones = digits[4]           # единицы
    
    try:
        step1 = tens ** ones  # десятки в степени единиц
        step2 = step1 * hundreds  # умножаем на сотни
        step3 = step2 / (ten_thousands - thousands)  # делим на разность
    except ZeroDivisionError:
        print("Случилось деление на ноль, выходим из программы")
        input("Нажмите Enter для продолжения...")
        return
    # Выводим подробное решение
    print("\n" + "=" * 50)
    print("ПОДРОБНОЕ РЕШЕНИЕ:")
    print("=" * 50)
    print(f"Исходное число: {num_int}")
    print(f"Разряды: {ten_thousands}(дес.тыс) {thousands}(тыс) {hundreds}(сот) {tens}(дес) {ones}(ед)")
    print(f"\n1. {tens}(десятки) ^ {ones}(единицы) = {tens} ^ {ones} = {step1}")
    print(f"2. {step1} × {hundreds}(сотни) = {step2}")
    print(f"3. {step2} / ({ten_thousands} - {thousands}) = {step2} / ({ten_thousands - thousands}) = {step3}")
    print("=" * 50)
    print(f"\nРЕЗУЛЬТАТ: {step3}")
    print("=" * 50)
    input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()