import io
import lesson3 as l3

programs = [
    ['Урок № 3 - Бэкенд ветеринарки', l3],
    ['Урок № 3 - Бэкенд ветеринарки', l3],
    ['Урок № 3 - Бэкенд ветеринарки', l3],
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
