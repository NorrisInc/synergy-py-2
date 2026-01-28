import io

defaultQuestions = [
    # Правильный ответ, Ответ пользователя
    ["Australopithecus", ""],
    ["Homo habilis", ""],
    ["Homo erectus", ""],
    ["Homo heidelbergensis", ""],
    ["Homo sapiens", ""],]

questions = []

def main():
    print("Урок 3.2 - Тест по биологии")
    questions = defaultQuestions

    for i, (index, _) in enumerate(questions):
        questions[i][1] = input(f"Стадия № {(i + 1)}: ")

    grade = 0
    for i, (answer, question) in enumerate(questions):
        if answer == question:
            grade = grade + 1
    if grade < 2:
        grade = 2
    print(f'\nОценка: {grade}')

if __name__ == "__main__":
    main()