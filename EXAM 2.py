# EXAM EXERCISES
# 1. Create a function that finds n number of prime numbers.
# RU: Создайте функцию, которая находит n количество простых чисел.
# 2. Create a function that counts how much time that 
# function takes to execute.
# RU: Создайте функцию, которая подсчитывает, сколько 
# времени занимает выполнение этой функции.
# 3. Create a class that takes this function as a method 
# and returns the execution time. Then, create an object
# and call the method.
# RU: Создайте класс, который принимает эту функцию в 
# качестве метода и возвращает время выполнения. Затем
# создайте объект и вызовите метод.
# EXAM EXERCISES
# 1. Create a function that finds n number of prime numbers.
# RU: Создайте функцию, которая находит n количество простых чисел.
# 2. Create a function that counts how much time that 
# function takes to execute.
# RU: Создайте функцию, которая подсчитывает, сколько 
# времени занимает выполнение этой функции.
# 3. Create a class that takes this function as a method 
# and returns the execution time. Then, create an object
# and call the method.
# RU: Создайте класс, который принимает эту функцию в 
# качестве метода и возвращает время выполнения. Затем
# создайте объект и вызовите метод.


# def prime_numbers(n):
#     result = []
#     current_num = 1
#         # METHOD 1
#     while len(result) < n:
#         current_num += 1
        # METHOD 1
        # for i in range(2, current_num):
        #     if current_num % i == 0:
        #         break
        # else:
        #     result.append(current_num)
        # -------------------------------
        # METHOD 2
        # if current_num % 2 != 0 and current_num % 3 != 0 and current_num % 5 != 0 and current_num % 7 != 0:
        #     result.append(current_num)
        # -------------------------------
        # METHOD 3
    #     if all(current_num % i != 0 for i in range(2, current_num)):
    #         result.append(current_num)

    # return result
    
    
    
    
    
# ЭКЗАМЕН - ТЕСТ: https://proglib.io/tests/test-na-znanie-yazyka-python

# ВОПРОС 1 / 15
# 🔢 Имеется кортеж вида T = (4, 2, 3). Какая из операций приведёт к тому, что имя T будет ссылаться на кортеж (1, 2, 3)?
# Поскольку кортежи неизменяемы, их нельзя модифицировать на месте, но мож­но создать новый кортеж с желаемым значением.
# Изменить первый элемент можно за счёт создания нового кортежа из частей имеющегося с помощью срезов и конкатенации:
# Т = (1,) + Т [1: ].При этом одноэлементные кортежи требуют хвостовой запятой, иначе число в скобках это всего лишь число.

# ВОПРОС 2 / 15
# 🔃 Для чего в Python используется встроенная функция enumerate()?
# Часто в коде начинающих разработчиков на Python можно встретить объявление for-цикла в виде for i in range(len(numbers))
# когда можно обойтись for num in numbers. Если в коде действительно необходим и сам элемент, и его индекс, используйте 
# enumerate().

# ВОПРОС 3 / 15
# 🌀 Что выведет интерпретатор для следующей программы (версия Python 3.6+)?
# f-строки – удобный способ отображения информации в нужном формате. Здесь на место {name} подставляется переменная name,
# а на место {age / 10:.5f} переменная age, деленная на 10. В форматировании указано представление с 5 знаками после запятой.

# ВОПРОС 4 / 15
# 🔂 Необходимо собрать и вывести все уникальные слова из строки рекламного текста.
# Какой из перечисленных типов данных Python подходит лучше всего?
# Множество (set) хранит только уникальные значения. Поэтому такой тип данных
# является лучшим кандидатом для решения указанной задачи – все повторяющиеся (неуникальные) значения будут отброшены.

# ВОПРОС 5 / 15
# 🐘 Учёт зверей в зоопарке ведётся с помощью приведённого ниже списка словарей.
# Какая из строчек кода выведет структуру, отсортированную в порядке увеличения возрастов животных?
# animals = [
#     {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
#     {'type': 'elephant', 'name': 'Devon', 'age': 3},
#     {'type': 'puma', 'name': 'Moe', 'age': 5},
# ]
# sorted(animals, key=lambda animal: animal['age'])
# У функции sorted есть необязательный аргумент key, позволяющий указать функцию,
# вызываемую перед сортировкой для каждого элемента. Для указанной задачи можно использовать
# лямбда-функцию вида lambda animal: animal['age']. Вместо animal можно использовать и просто x , 
# это лишь обозначение передаваемого элемента. Для каждого элемента будет вызываться ключ 'age', 
# и уже по его значению будет происходить сортировка элементов списка animals.

# ВОПРОС 6 / 15
# 💬  Какой результат выведет следующий код?
# def f(a, *pargs, **kargs): print(a, pargs, kargs)
# f(1, 2, 3, x=4, y=5)
# В этом примере используются операторы * и **, предназначенные для подде­ржки функций,
# которые принимают неизвестное заранее количество аргументов. Первый оператор (*) собирает в кортеж
# несопоставленные позиционные аргументы. Второй оператор (**) собирает словарь по ключевым аргументам.
# Поэтому правильный ответ: 1 (2, 3) {'x': 4, 'y': 5}.Так как инструкция имеет однострочный характер,
# отсутствие переноса строки не является ошибкой.

# ВОПРОС 7 / 15
# 📜 Как вывести список методов и атрибутов объекта x?
# help(x)
# info(x)
# ?x
# dir(x)
# Правильный ответ – функция dir. Функция help выводит справку по объекту,
# доступную из строк документации, а остальные примеры не являются частью стандартной библиотеки Python.

# ВОПРОС 8 / 15
# 🔄 Как можно более кратко представить следующую запись?
# if X:
#     A = Y
# else:
#     A = Z
# Здесь мы видим обычное тернарное выражение if/else, которое, например, часто встречается в генераторах.
# Правильным ответом является A = Y if X else Z.

# 9 / 15
# ♻️ Какая из перечисленных инструкций выполнится быстрее всего, если n = 10**6?
# В круглых скобках (i for i in range(n)) «чистое» выражение-генератор. Оно не загружает в память коллекцию,
# поэтому присваивание происходит быстрее остальных случаев, ведь сами элементы последовательности не создаются.
# В остальных случаях происходит создание коллекций «на месте».