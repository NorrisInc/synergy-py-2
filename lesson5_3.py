import io

def main():
    print("Урок 5.3 - Анализ инвестиций")
    print("=" * 50)
    
    try:
        # Ввод данных
        X = int(input("\nМинимальная сумма инвестиций X = "))
        A = int(input("Сумма у Майкла A = "))
        B = int(input("Сумма у Ивана B = "))
        
        # Вычисляем
        mike_can = A >= X
        ivan_can = B >= X
        together_can = (A + B) >= X
        
        # Создаем таблицу возможностей
        print("\nТАБЛИЦА ВОЗМОЖНОСТЕЙ:")
        print("-" * 40)
        print(f"Сценарий                 | Возможно? | Не хватает")
        print("-" * 40)
        print(f"Майкл один               | {'✓' if mike_can else '✗':^9} | {max(0, X - A)}$")
        print(f"Иван один                | {'✓' if ivan_can else '✗':^9} | {max(0, X - B)}$")
        print(f"Вместе                   | {'✓' if together_can else '✗':^9} | {max(0, X - (A + B))}$")
        print("-" * 40)
        
        # Определяем результат
        print(f"\nВОЗМОЖНЫЕ ВАРИАНТЫ:")
        
        if mike_can and ivan_can:
            print("   1. Майкл инвестирует один")
            print("   2. Иван инвестирует один")
            print("   3. Оба инвестируют вместе")
            print("\n   РЕЗУЛЬТАТ: 2")
            result = 2
            
        elif mike_can and not ivan_can:
            print("   1. Майкл инвестирует один")
            if together_can:
                print("   2. Могут инвестировать вместе")
            print("\n   РЕЗУЛЬТАТ: Mike")
            result = "Mike"
            
        elif not mike_can and ivan_can:
            print("   1. Иван инвестирует один")
            if together_can:
                print("   2. Могут инвестировать вместе")
            print("\n   РЕЗУЛЬТАТ: Ivan")
            result = "Ivan"
            
        elif not mike_can and not ivan_can and together_can:
            print("   1. Могут инвестировать только вместе")
            print(f"      Майкл: {A}$, Иван: {B}$, Вместе: {A + B}$")
            print(f"      Не хватало по отдельности: Майклу {X - A}$, Ивану {X - B}$")
            print("\n   РЕЗУЛЬТАТ: 1")
            result = 1
            
        else:
            print("   Невозможные варианты:")
            print(f"      • Майкл один: не хватает {X - A}$")
            print(f"      • Иван один: не хватает {X - B}$")
            print(f"      • Вместе: не хватает {X - (A + B)}$")
            print("\n   РЕЗУЛЬТАТ: 0")
            result = 0
        
        input("Нажмите Enter для продолжения...")
        return result
        
    except ValueError:
        print("Ошибка: введите целые числа!")
        input("Нажмите Enter для продолжения...")
        return

if __name__ == "__main__":
    main()
