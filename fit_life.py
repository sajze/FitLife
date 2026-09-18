WATER_PER_KG = 30  # мл воды на кг веса
WATER_L = 1000  # мл в литре

print('Вас приветствует FitLife!')

while True:
    user_name = input('Введите ваше имя: ')
    if user_name.strip():
        break
    print('Неверное имя. Пожалуйста, введите корректное значение.')

while True:
    user_age = int(input('Введите ваш возраст: '))
    if 0 < user_age < 150:
        break
    print('Неверный возраст. Пожалуйста, введите корректное значение.')

while True:
    user_weight = float(input('Введите ваш вес (в кг): '))
    if 0 < user_weight < 800:
        break
    print('Неверный вес. Пожалуйста, введите корректное значение.')

while True:
    user_height = float(input('Введите ваш рост (в м): '))
    if 0 < user_height < 3:
        break
    print('Неверный рост. Пожалуйста, введите корректное значение.')

# Вычисляем ИМТ
bmi = user_weight / (user_height ** 2)

# Вычисляем рекомендуемое количество воды в мл
water_ml = user_weight * WATER_PER_KG

# Преобразуем количество воды из мл в литры
water_l = water_ml / WATER_L

print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Ваш ИМТ: {round(bmi, 1)}')
print(f'Рекомендуемая норма воды: {water_l} л. в день.')
