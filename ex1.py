#Напишите функцию, которая будет принимать номер кредитной карты и
#показывать только последние 4 цифры. Остальные цифры должны заменяться
#звездочками
import random
def card(number):

    n = '*' * len(number[:-4]) + number[-4:]

    return n


print(card('1234567891234567'))
