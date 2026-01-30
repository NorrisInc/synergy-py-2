import io
import os
import platform
import lesson3_1 as l3_1
import lesson3_2 as l3_2
import lesson4_1 as l4_1
import lesson4_2 as l4_2
import lesson5_1 as l5_1
import lesson5_2 as l5_2
import lesson5_3 as l5_3
import lesson6_1 as l6_1
import lesson6_2 as l6_2
import lesson6_3 as l6_3
import lesson7_1 as l7_1
import lesson7_2 as l7_2
import lesson8_1 as l8_1
import lesson8_2 as l8_2
import lesson8_3 as l8_3
import lesson9_1 as l9_1
import lesson9_2 as l9_2
import lesson9_3 as l9_3
import lesson10_1 as l10_1
import lesson10_2 as l10_2

programs = [
    ['Урок № 3.1 - Бэкенд ветклиники', l3_1],
    ['Урок № 3.2 - Тест по биологии', l3_2],
    ['Урок № 4.1 - Площадь и периметр', l4_1],
    ['Урок № 4.2 - Пятизначное число', l4_2],
    ['Урок № 5.1 - Анализ числа', l5_1],
    ['Урок № 5.2 - Анализ слова', l5_2],
    ['Урок № 5.3 - Анализ инвестиций', l5_3],
    ['Урок № 6.1 - Циклы: поиск нулевых значений', l6_1],
    ['Урок № 6.2 - Циклы: натуральные делители', l6_2],
    ['Урок № 6.3 - Циклы: отрезок и четные числа', l6_3],
    ['Урок № 7.1 - Строки: палиндромы', l7_1],
    ['Урок № 7.2 - Строки: убрать лишние пробелы', l7_2],
    ['Урок № 8.1 - Списки: переворот массива', l8_1],
    ['Урок № 8.2 - Списки: перетасовка массива', l8_2],
    ['Урок № 8.3 - Списки: лодки и рыбаки', l8_3],
    ['Урок № 9.1 - Множества: разные числа', l9_1],
    ['Урок № 9.2 - Множества: два списка', l9_2],
    ['Урок № 9.3 - Множества: поиск дубликатов', l9_3],
    ['Урок № 10.1 - Словари: ветклиника', l10_1],
    ['Урок № 10.2 - Словари: ключ и значение в степени ключа', l10_2],
]

def clear_console():
    """Очищает консоль в зависимости от операционной системы"""
    if platform.system() == "Windows":
        os.system('cls')
    else: 
        os.system('clear')

def main():
    while True: 
        print(f"Список уроков:")
        for i, program in enumerate(programs, 1):
            print(f"{i}. {program[0]}")
        try:
            programId = int(input("Введите номер урока (0 выйти из программы): ").strip())
        except ValueError:
            print("Ошибка: Введите число!")
            continue
        if(programId < 1):
            break
        if 1 <= programId <= len(programs):
            clear_console()
            print(f"Выбран урок: {programs[programId - 1][0]}")
            programs[programId - 1][1].main()
        else:
            print(f"Ошибка: Нет урока с номером {programId}")
        clear_console()
    print("Выполнение программы завершено успешно")

if __name__ == "__main__":
    main()
