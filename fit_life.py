print('Вас приветствует FitLife!')
user_name = input('Введите ваше имя: ')
user_age = int(input('Введите ваш возраст: '))
user_weight = float(input('Введите ваш вес (в кг): '))
user_height = float(input('Введите ваш рост (в м): '))
bmi = user_weight / (user_height ** 2)
water_ml = user_weight * 30
water_l = water_ml / 1000
print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Ваш ИМТ: {round(bmi, 1)}')
print(f'Рекомендуемая норма воды: {water_l} л. в день.')
