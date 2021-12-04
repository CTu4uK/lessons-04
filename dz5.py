# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

list = [i for i in range(100, 1001, 2)]
print("Список чётных чисел в диапазоне [100..1000]:\n", list)
print("Произведение всех элементов списка:\n", reduce(lambda x,y: x*y, list))