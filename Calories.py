def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        print("Некорректный ввод. Попробуйте снова.")


def is_numeric_input(user_input):
    return user_input.replace('.', '', 1).isdigit()


def is_positive_numeric_input(user_input):
    return is_numeric_input(user_input) and float(user_input) > 0


def is_valid_gender(user_input):
    return user_input.lower() in ["мужской", "женский"]


def is_valid_activity_level(user_input):
    return user_input in ["1", "2", "3", "4", "5"]


# Ввод данных
gender = get_valid_input("Введите свой пол (мужской, женский): ", is_valid_gender)
age = float(get_valid_input("Введите свой возраст (полных лет): ", is_positive_numeric_input))
weight = float(get_valid_input("Введите свой вес (кг): ", is_positive_numeric_input))
height = float(get_valid_input("Введите свой рост (см): ", is_positive_numeric_input))
activity_level = get_valid_input("Введите уровень активности (1-5): ", is_valid_activity_level)

# Подсчет количества калорий
activity_level_mapping = {"1": 1.2, "2": 1.375, "3": 1.55, "4": 1.725, "5": 1.9}
activity_level = activity_level_mapping[activity_level]

if gender == "мужской" and 13 <= age < 80:
    amount_calories = (10 * weight + 6.25 * height - 5 * age + 5) * int(activity_level)
elif gender == "женский" and 13 <= age < 80:
    amount_calories = (10 * weight + 6.25 * height - 5 * age - 161) * int(activity_level)
else:
    print("Выход из программы, так как данные некорректны")
    exit()

# Вывод данных
print("Пол:", gender)
print("Возраст:", age)
print("Вес:", weight)
print("Рост:", height)
print("Необходимое количество килокалорий (ккал) в сутки: ", amount_calories)
