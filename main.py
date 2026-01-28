import io
import lesson3_1 as l3_1
import lesson3_2 as l3_2

programs = [
    ['Урок № 3.1 - Бэкенд ветеринарки', l3_1],
    ['Урок № 3.2 - Тест по биологии', l3_2],
    ['Урок № 3 - Бэкенд ветеринарки', l3_1],
]

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
            print(f"Выбран урок: {programs[programId - 1][0]}")
            programs[programId - 1][1].main()
        else:
            print(f"Ошибка: Нет урока с номером {programId}")

if __name__ == "__main__":
    main()
