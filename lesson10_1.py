import io

def get_age_word(age):
    try:
        age_int = int(age)
        if age_int % 10 == 1 and age_int % 100 != 11:
            return "год"
        elif 2 <= age_int % 10 <= 4 and (age_int % 100 < 10 or age_int % 100 >= 20):
            return "года"
        else:
            return "лет"
    except:
        return "лет"

def main():
    print("Урок 10.1 - Словари: ветклиника")
    print("=" * 50)
    try:
        pets = {}
        pet_name = input("Имя питомца: ").strip()
        pet_type = input("Вид питомца: ").strip()
        pet_age = int(input("Возраст питомца (число): ").strip())
        owner_name = input("Имя владельца: ").strip()
        pets[pet_name] = {
            "Вид питомца": pet_type,
            "Возраст питомца": pet_age,
            "Имя владельца": owner_name
        }
        # получаем данные через keys() и values()
        pet_key = list(pets.keys())[0]
        pet_values = list(pets.values())[0]
        vid = pet_values["Вид питомца"]
        age = pet_values["Возраст питомца"]
        owner = pet_values["Имя владельца"]
        print(f'Это {vid} по кличке "{pet_key}". Возраст питомца: {age} {get_age_word(age)}. Имя владельца: {owner}')
    except ValueError:
        print("Ошибка: нужно вводить числа")
    input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()