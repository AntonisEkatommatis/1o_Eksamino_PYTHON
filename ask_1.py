#Ergasia 1
#Antonis Ekatommatis
#Eisagwgh sthn episthmh twn ypologistwn
#1o Eksamino

#Dimiourgia Synartisis
def sumIntervals (L):
    a=[]
    b=[]
    asin=0
    bsin=0
    apot=0
    #Eisagawgi sthn lista a oles tis arxes apo ta oria
    for i in range(len(L)):
        a.append(L[i][0])
    #Eisagwgi sthn lista b ta teleutaia psifia kathe oriou
    for i in range(len(L)):
        b.append(L[i][1])
    #Bubblesort
    N=len(a)
    for i in range(1,N,1):
        for j in range(N-1,i-1,-1):
            if a[j] < a[j-1]:
                a[j],a[j-1]=a[j-1],a[j]
                b[j],b[j-1]=b[j-1],b[j]
    #Elegxoi gia na vgei to athroisma
    for i in range(1,len(a)):
        while a[i] < b[i-1]:
            a[i]=a[i]+1
    for i in range(len(a)):
        while a[i] > b[i]:
            b[i]=b[i]+1
    for item in a:
        asin+=item
    for item in b:
        bsin+=item
    apot=bsin-asin
    return apot


print sumIntervals([[1,2], [6, 10], [11, 15]])
print sumIntervals([[1,4], [7, 10], [3, 5]])
print sumIntervals([[1,5], [10, 20], [1, 6], [16, 19], [5, 11]])
