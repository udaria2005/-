import numpy as np
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [3, 5, 6, 7, 2, 4, 1, 8, 4]
a = np.array(a)
b = np.array(b)
a = a.reshape(3,3)
b = b.reshape(3,3)
print(a)
print(a.max())     #максимум
print(a.sum())     #сумма всех членов
c = np.insert(a,2,9)    #вставить после нного элемента
print(c)
print(np.sort(a))    #от меньшего к большему
print(np.linalg.det(a))    #определитель
print(np.transpose(a))    #транспонировать
print(a.dot(b))          #умножает а на б
print(np.linalg.inv(a))   #обратная матрица
z,d = (np.linalg.eig(a))  #z - собственные значения d - собственые векторы, 
#соответствующие собственным значениям, записаны по столбцам
print(d)
print(a.min())              #минимум
#матрица в новых координатах = (матрица перехода)^(-1)*наша матрица в старых
#координатах*матрица переход