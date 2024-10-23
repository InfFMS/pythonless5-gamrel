# Массив имеет четное число элементов N.
# Заполнить массив случайными числами и
# выполнить реверс отдельно в первой половине и второй половине.
# Пример: ввод N = 6
# [1,2,3,4,5,6]
# Вывод: [3,2,1,6,5,4]
import random
a=0
l=[]
N=int(input())
while a<N:
    a+=1
    l+= [random.randint(0, 100)]
print (l)
a=0
b=l[::]
while a<N/2:
    b.pop(N-a-1)
    a+=1
a=0
c=b[::]
b=l[::]
while a<N/2:
    b.pop(a)
    a+=1
c = list(reversed(c))
b = list(reversed(b))
print (c+b)
