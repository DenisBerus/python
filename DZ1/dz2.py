#Второй семинар
"""
#Задание 1: Поставьте оценку!

rating = int(input('Введите число:'))
goodreview = 0
nogoodreview = 0
while rating != 0:
    if rating > 0:
        goodreview += 1
    else:
        nogoodreview += 1

    rating = int(input('Введите число:'))

print('Кол-во положительных чисел:', goodreview)
print('Кол-во отрицательных чисел:', nogoodreview)

"""
"""
#Задача 2. Обычный день на работе

""""""
hour = 0
tasks_sum = 0
go_to_store = False

print('Начался 8-часовой рабочий день')
while hour != 8:
    hour += 1
    print(hour, 'час')

    tasks = int(input('Сколько задач решит Максим? '))
    tasks_sum += tasks

    call = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет):'))
    if call == 1:
        go_to_store = True 

    print('Итого Максим выполнил задач:', tasks_sum)
    if go_to_store:
        print('Нужно зайти в магазин')
"""
