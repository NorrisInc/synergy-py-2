import io

def main():
    print("Урок 8.2 - Списки: перетасовка массива")
    try:
        n = input("Введите N число в соответствии с 1 ≤ N ≤ 100 000: ")
        n = int(n)

        # Читаем числа
        s = input("Введите N чисел через пробел в соответствии с1 ≤ Ai ≤ 10e9:\n")
        arr = s.split()

        # Меняем местами
        new_arr = []
        if len(arr) > 0:
            new_arr.append(arr[-1])  # Последний становится первым
            
        for i in range(len(arr) - 1):
            new_arr.append(arr[i])   # Остальные по порядку

        # Выводим
        print("Вывод:")
        for x in new_arr:
            print(x, end=" ")
    except ValueError:
        print("Ошибка: нужно вводить числа")
    input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
