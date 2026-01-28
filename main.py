import io
import os
import platform
import lesson3_1 as l3_1
import lesson3_2 as l3_2
import lesson4_1 as l4_1
import lesson4_2 as l4_2
import lesson5_1 as l5_1
import lesson5_2 as l5_2

programs = [
    ['Урок № 3.1 - Бэкенд ветеринарки', l3_1],
    ['Урок № 3.2 - Тест по биологии', l3_2],
    ['Урок № 4.1 - Площадь и периметр', l4_1],
    ['Урок № 4.2 - Пятизначное число', l4_2],
    ['Урок № 5.1 - Анализ числа', l5_1],
    ['Урок № 5.2 - Анализ слова', l5_2],
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

if __name__ == "__main__":
    main()
