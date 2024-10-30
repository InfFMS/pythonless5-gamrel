# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]
import random
a=0
l=[]
L=[]
q=[]
n=1
i=0
k=0
c=0
K=0
N=int(input())
P=N
while a<N:
    a+=1
    l+= [random.randint(10, 100000)]
a=0
#print (l)
while i<N:
    while l[i]>n:
        n*=10
        K=n
        c=n
    #print(n)
    while n>0.1:
        while i < 10:
            while n>0.1:
                k+=i*n
                n /= 10
            i += 1
            L.append(k)
            k=0
            n=c
        i=0
        a+=1
        c=K*10**(-a)
    N-=1
k=0
i=0
#print(L)
while i<P:
    while k<len(L):
        if(l[i]==L[k]): q.append(L[k])
        k+=1
    i+=1
    k=0
print(q)





