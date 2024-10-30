# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]
import random
a=0
l=[]
N=int(input())
while a<N:
    a+=1
    l+= [random.randint(0, 100)]
print (l)
a=0
n=0
j=0
while a<N:
    while n<N:
        if (l[a]==l[n]) and (a!=n) and (a<n):
            j+=1
            del l[n]
            N-=1
        n+=1
    j=0
    n=0
    a+=1
print(l)
print(len(l))