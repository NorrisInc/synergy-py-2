import io

def main():
    print("Урок 7.1 - Строки: палиндромы")
    print("=" * 50)
    
    # Ввод строки
    word = input("Введите строку (без пробелов): ").strip()
    
    if not word:
        print("Ошибка: строка не может быть пустой!")
        input("Нажмите Enter для продолжения...")
        return
    
    print(f"\nАнализируем строку: '{word}'")
    print(f"Длина строки: {len(word)} символов")
    
    # Проверяем на палиндром
    if word == word[::-1]:
        print("Результат: yes")
        print(f"\nСтрока '{word}' является палиндромом!")
        
        # Дополнительная информация
        print(f"\nПроверка:")
        print(f"   Оригинал: {word}")
        print(f"   Обратная: {word[::-1]}")
        print(f"   Совпадают: {'Да' if word == word[::-1] else 'Нет'}")
    else:
        print("Результат: no")
        print(f"\nСтрока '{word}' НЕ является палиндромом")
        
        # Показываем различия
        print(f"\nСравнение:")
        print(f"   Оригинал: {word}")
        print(f"   Обратная: {word[::-1]}")
        
        # Находим первую позицию различия
        for i in range(len(word)):
            if word[i] != word[-(i+1)]:
                print(f"\n   Первое различие на позиции {i}:")
                print(f"      Оригинал: '{word[i]}' (позиция {i})")
                print(f"      Обратная: '{word[-(i+1)]}' (позиция {len(word)-i-1})")
                break
    print(f"Явяляется ли палиндромом: {word == word[::-1]}")
    input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
