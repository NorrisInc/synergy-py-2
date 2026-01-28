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
    species = input("Вид питомца: ").strip()
    name = input("Кличка: ").strip()
    age = input("Возраст (в годах): ").strip()

    print(f'\nЭто {species} по кличке "{name}". Возраст: {age} года.')

if __name__ == "__main__":
    main()