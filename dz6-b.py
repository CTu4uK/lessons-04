# 6. Реализовать два небольших скрипта:
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
# быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также
# необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import cycle

import length as length

list = [5, 3, 3, 1, 0, 4, 2, 4, 7, 3]

for i in list:
	print(i, end=' ')
