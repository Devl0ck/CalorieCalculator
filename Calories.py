def get_user_input(prompt, is_numeric=False):  # Проверка на правильность введенных данных
    while True:
        user_input = input(prompt)
        if is_numeric:
            try:
                user_input = float(user_input)
                return user_input
            except ValueError:
                print("Введено не число. Попробуйте снова.")
                continue
        if user_input:
            return user_input
        print("Поле не может быть пустым. Попробуйте снова.")


# Ввод данных
while True:
    gender = get_user_input("Введите свой пол (мужской, женский, другой): ")
    if gender.lower() in ["мужской", "женский", "другой"]:
        break
    print("Некорректный пол. Попробуйте снова.")

age = get_user_input("Введите свой возраст: ", is_numeric=True)
weight = get_user_input("Введите свой вес: ", is_numeric=True)
height = get_user_input("Введите свой рост: ", is_numeric=True)

while True:
    activity_level = get_user_input("Введите уровень активности (сидячий, умеренный, активный): ")
    if activity_level.lower() in ["сидячий", "умеренный", "активный"]:
        break
    print("Некорректный уровень активности. Попробуйте снова.")

# Вывод данных
print("Пол:", gender)
print("Возраст:", age)
print("Вес:", weight)
print("Рост:", height)
print("Уровень активности:", activity_level)
