#Ergasia 12
#Antonis Ekatommatis
#Eisagwgh sthn episthmh twn ypologistwn
#1o Eksamino
ABC="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
C=[]
N=[]
Y=[]
P=[]

fin=open("ask12.txt","r")
lines=fin.readlines()
fin.close()

for i in range(len(lines)):
    lines[i]=lines[i].upper()
    
L="".join(lines)

for letter in ABC:
    if letter in L:
        C.append(letter)
        x=L.count(letter)
        N.append(x)

Length_C=len(C)
for i in range(1,Length_C,1):
        for j in range(Length_C-1,i-1,-1):
            if N[j] > N[j-1]:
                N[j],N[j-1]=N[j-1],N[j]
                C[j],C[j-1]=C[j-1],C[j]

for i in range(1,Length_C,1):
        for j in range(Length_C-1,i-1,-1):
            if N[j] < N[j-1]:
                N[j],N[j-1]=N[j-1],N[j]

for char in L:
    Y.append(char)

D=-1

CH="".join(C)

counter=0

for i in range(len(Y)):
    P.append(Y[i])

for i in range(len(N)):
    for j in range(len(Y)):
        if Y[j] == C[i]:
            P[j]=C[D]
    D=D-1

final="".join(P)
                
fin=open("ask12.txt","w")
fin.write(final)
fin.close()


    
