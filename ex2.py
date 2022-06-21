#Напишите функцию, которая проверяет: является ли слово палиндромом
def pal(letter):
    if letter == letter[::-1]:
        print('Является палиндромом')
    else:
        print('Не является палиндромом')
    return letter

print(pal(input('Введите слово: ')))