import io

def main():
    print("Урок 5.2 - Анализ слова")
    print("=" * 50)
    
    # Ввод слова
    word = input("Введите слово из маленьких латинских букв: ").strip().lower()
    
    # Проверка, что слово состоит только из латинских букв
    if not word.isalpha() or not word.islower():
        print("Ошибка: слово должно состоять из маленьких латинских букв!")
        input("Нажмите Enter для продолжения...")
        return
    
    # Определяем гласные
    vowels = 'aeiou'
    
    # Счетчики
    vowel_count = 0
    consonant_count = 0
    
    # Счетчики для каждой гласной
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Анализируем каждую букву
    for letter in word:
        if letter in vowels:
            vowel_count += 1
            vowel_counts[letter] += 1
        else:
            consonant_count += 1
    
    # Вывод результатов
    print(f"\nАНАЛИЗ СЛОВА '{word}':")
    print(f"   Длина слова: {len(word)} букв")
    print(f"   Гласных букв: {vowel_count}")
    print(f"   Согласных букв: {consonant_count}")
    print(f"   Соотношение: {vowel_count}:{consonant_count}")
    
    print("\nРАСПРЕДЕЛЕНИЕ ГЛАСНЫХ:")
    for vowel in vowels:
        count = vowel_counts[vowel]
        if count > 0:
            print(f"   '{vowel}': {count} раз(а)")
        else:
            print(f"   '{vowel}': False")
    
    print("=" * 50)
    input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
