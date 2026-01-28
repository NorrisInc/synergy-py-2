import io

arr = []

def main():
    print("Урок 3.2 - Тест по биологии")
    i = 0
    while True:
        i = i + 1
        inp = input(f"Введите стадию {i}: ")
        if (inp == ""):
            break
        arr.append(inp)
        if (inp.lower() == "homo sapiens"):
            break
    print(*arr, sep = " => ")
    input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()