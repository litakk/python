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

# ВОПРОС - 1
# 🔢 Имеется кортеж вида T = (4, 2, 3). Какая из операций приведёт к тому, что имя T будет ссылаться на кортеж (1, 2, 3)?
# Поскольку кортежи неизменяемы, их нельзя модифицировать на месте, но мож­но создать новый кортеж с желаемым значением.
# Изменить первый элемент можно за счёт создания нового кортежа из частей имеющегося с помощью срезов и конкатенации:
# Т = (1,) + Т [1: ].При этом одноэлементные кортежи требуют хвостовой запятой, иначе число в скобках это всего лишь число.

# ВОПРОС - 2
# 🔃 Для чего в Python используется встроенная функция enumerate()?
# Часто в коде начинающих разработчиков на Python можно встретить объявление for-цикла в виде for i in range(len(numbers))
# когда можно обойтись for num in numbers. Если в коде действительно необходим и сам элемент, и его индекс, используйте 
# enumerate().

# ВОПРОС - 3
# 🌀 Что выведет интерпретатор для следующей программы (версия Python 3.6+)?
# f-строки – удобный способ отображения информации в нужном формате. Здесь на место {name} подставляется переменная name,
# а на место {age / 10:.5f} переменная age, деленная на 10. В форматировании указано представление с 5 знаками после запятой.

