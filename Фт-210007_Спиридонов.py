from random import choice
import logging

logging.basicConfig(filename = "base_log.log", level=logging.INFO)

# Ввод
while True:
    n = int(input('Введите число N (начиная от 2): '))
    if n > 1:
        break
    else:
        print('Введите корректное значение!')

# Наполнение мешка с бочонками
bag = []
for i in range(1, n + 1):
    bag.append(i)

# Выбор бочонка из мешка + его удаление
def getNumber(num):
    logging.info(f"getNumber: {num}")
    print('Вы вытащили бочонок с номером: ', num)
    del bag[bag.index(num)]

# Нажатие кнопки 
while len(bag) > 1:
    while True:
        button = input('Нажать кнопку? (да или нет): ').lower()
        if button == 'да' or button == 'нет':
            break
        else:
            print('Введите корректную строку! (да или нет)')
    if button == 'да':
        logging.info("Button is click")
        random_number = choice(bag)
        getNumber(random_number)
    elif button == 'нет':
        logging.info("Button is not click")
        break

if len(bag) == 1:   
    print('Последний бочонок в мешке c номером: ', bag[0])
    print('Мешок пуст')

print('Программа завершена')
