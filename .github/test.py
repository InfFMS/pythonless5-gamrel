import random
a=0
l=[]
N=int(input())
while a<N:
    a+=1
    l+= [random.randint(0, 100)]
print (l)
a=0
k=0
n=0
i=0
j=0
q=0
while a<N:
    while n<N:
        if (l[a]==l[n]) and (a!=n) and (a<n):
            print('значение:',l[n],'индекс:', n+q)
            k+=1
            i+=1
            j+=1
            if j>1 :
                del l[n]
                N-=1
        if i != 0 and j < 2:
            print('значение:', l[a], 'индекс:', a)
        i=0
        n+=1
    j=0
    n=0
    a+=1
if k==0: print('No')
else:print('Yes')

#править