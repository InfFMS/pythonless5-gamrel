# Заполните список длины N случайными числами в диапазоне от 0 до 1000
# Выведите:
# 1.длину списка;
# 2.последний элемент списка;
# 3.список в обратном порядке (вспоминаем срезы);
# 4.YES, если список содержит трехзначное число, состоящее из одинаковых цифр
# NO в противном случае;
# 5.список с удаленными первым и последним элементами.
import random
N = int(input())
l=[]
a=0
while a<N:
    a+=1
    l+= [random.randint(0, 1000)]
print (l)
print (len(l))
print (l[N-1])
k=list(reversed(l))
print(k) #3
i=0
k=0
while i<N:
    if (l[i]== 111)or(l[i]== 222)or(l[i]== 333)or(l[i]== 444)or(l[i]== 555)or(l[i]== 666)or(l[i]== 777)or(l[i]== 888)or(l[i]== 999):
        print ('yes')
        k-=1
    i+=1
    k+=1
if k==i: print ('No')
l.pop(0)
l.pop(-1)
print (l)
#5
