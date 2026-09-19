from math import *
n = int(input())
c = int(input())
z = int(input())
zap = n*c
sr = z//zap+1
sk = ceil((z-(zap*(sr-1)))/c)
stl = int((z-(zap*(sr-1)))/sk)
print(f'страница {sr} столбец {stl} строка {sk}')

#В примере в выходных данных в задании было подсчитано так, что столбцов 25, а строк 5, я решила как по условию задания, что первое число это кол-во строк