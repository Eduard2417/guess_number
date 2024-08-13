from random import randint
number = randint(1, 100)

print('Привет')
while True:
    response = int(input('Введи число:'))

    if response == number:
        print('Ты угодал!')
        break
    elif response < number:
        print('Тысло больше')
    else:
        print('Число меньше')

print('Отличная интуиция! Вы угадали число :)')