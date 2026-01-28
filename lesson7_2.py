import io

def main():
    print("Урок 7.2 - Строки: убрать лишние пробелы")
    print("=" * 50)
    
    # Ввод строки
    text = input("Введите строку: ").strip()
    print("=" * 50)
    result = ' '.join(text.split())
    print(f"Изначальная строка: {text}")
    print(f"  длина строки: {len(text)}")
    print(f"\nРезультирующая строка: {result}")
    print(f"  длина строки: {len(result)}")
    input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
