# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
#
# 5 -> 1 0 1 1 0
# 2

# n = int(input('Введите количество монеток: '))
# count1 = 0
# count2 = 0
# for _ in range(n):
#     temp = int(input('1 если "орёл", 0 если "решко": '))
#     if temp != 0 and temp != 1:
#         print('Вы ввели не корректное значение')
#         break
#     if temp == 1:
#         count1 += 1
#     else:
#         count2 += 1
# if count1 < count2:
#     print(f'Переверните монеты с орлом {count1} раза')
# elif count1 == count2:
#     print(f'Количество монеток одинаковое')
# else:
#     print(f'Переверните монеты с решкой {count2} раза')





# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму
# этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
#
# 4 4 -> 2 2
# 5 6 -> 2 3

# a = int(input('Введите сумму чисел: '))
# b = int(input('Введите произведение чисел: '))
# c = 0
# for i in range(a + b):
#     if c:
#         break
#     for j in range(a + b):
#         if i + j == a and i * j == b:
#             c = 1
#             print(*sorted([i, j]))
#             break
#       ЧЕСТНО... Подсмотрел)





# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
#
# 10 -> 1 2 4 8

# n = int(input('Введите число N: '))
# res = 2
# constant = 2
# print(1)
# while res < n:
#     print(res)
#     res = res*constant







# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой
# для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но
# вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый
# тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза.
# Все числа натуральные и не превышают 30000.


# n = int(input('Введите количество арбузов: '))
# temp = int(input('Задайте вес арбуза: '))
# max_count = temp
# min_count = temp
# for _ in range(1, n):
#     temp = int(input('Задайте вес арбуза: '))
#     if temp > max_count:
#         max_count = temp
#     if temp < min_count:
#         min_count = temp
# print(f'Арбуз потяжелее {max_count}, арбуз полегче {min_count}')
