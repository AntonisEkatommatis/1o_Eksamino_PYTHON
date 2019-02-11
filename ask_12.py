ABC="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

C=[]
#C=Characters

N=[]
#N=Poses fores emfanizete kathe xaraktiras

Y=[]
#Lista pou periexei gramma gramma to keimeno tou arxeiou

P=[]
#Diplotipo tis listas Y pou sto telos 8a ginei to teliko string

#Anoigma arxeiou gia "r"
fin=open("ask12.txt","r")
#Dimiourgia listas lines pou periexei kathe grammi
lines=fin.readlines()
fin.close()
#Kleisimo tou arxeiou

for i in range(len(lines)):
    lines[i]=lines[i].upper()
    #Metatropi tou keimenou se kefalaia
 
L="".join(lines)
#L=Metatropi tis listas lines se string

for letter in ABC:
    if letter in L:
        C.append(letter)
        x=L.count(letter)
        N.append(x)
        #Evresi poses fores emfanizetai kathe xaraktiras tou alfavitou kai apothikeush sthn lista C ton xaraktira kai sthn lista N to poses fores emfanizetai

#Bubblesort gia taksinomisi na mpei prwtos sthn lista o xaraktiras pou emfanizete pio polles fores kai teleutaios autois pou emfanizetai ligoteres
Length_C=len(C)
for i in range(1,Length_C,1):
        for j in range(Length_C-1,i-1,-1):
            if N[j] > N[j-1]:
                N[j],N[j-1]=N[j-1],N[j]
                C[j],C[j-1]=C[j-1],C[j]


#Topothetisi to string L (pou einai to arxeio) xaraktira xaraktira sthn lista Y
for char in L:
    Y.append(char)

D=-1
#ksekinaei apo to telos kai ftanei stin arxh



#Duplicate List "P"
for i in range(len(Y)):
    P.append(Y[i])


for i in range(len(C)):
    for j in range(len(Y)):
        if Y[j] == C[i]:
            P[j]=C[D]
    D=D-1
    #Kanei elengxo gramma gramma kai vazei oti emfanizetai pio polles fores, me auto pou emfanizetai tis ligoteres

final="".join(P)
#Dimiourgia tis telikis listas se string, giati sta arxeia mporeis na kaneis write mono string

#Anoigma arxeiou auth thn fora gia "w" pou svinei ola ta ypolipa            
fin=open("ask12.txt","w")
#Topothetisi sto arxeio to teliko string
fin.write(final)
fin.close()
#Kleisimo tou arxeiou


    
