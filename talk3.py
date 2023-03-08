from random import randint

upper_limit = 1000
lower_limit = 0
num = randint(lower_limit, upper_limit)
count = 10
print('Загаданное число для контроля',num)

a = int(input('Введите число от 0 до 1000: '))
print()


while ( a != num):

    if a > num:
        count -=1
        print('Меньше. Осталось ' ,count, 'попыток')
        a = int(input('Уточните число: '))
        print()
    if a < num:
        count -=1
        print('Больше. Осталось ' ,count, 'попыток')
        a = int(input('Уточните число: '))
        print()
    if a == num:
        print('Угадали')

    if (count == 0):
        print('Вы проиграли')
        break

        continue

