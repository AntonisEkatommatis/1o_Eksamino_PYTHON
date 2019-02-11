#Ergasia 9
#Antonis Ekatommatis
#Eisagwgh sthn episthmh twn ypologistwn
#1o Eksamino
import itertools

#Meso tis vivliothikis itertools pairnw olous tous pithanous syndiasmous tis listas
#Vriskw to athroisma kathe syndiasmou, kai krataw ton megalytero syndiasmo me vasi to athroisma


def maxSequence(L):
    s=L[0]
    c=[]
    for i, j in itertools.combinations(range(len(L) + 1), 2):
        if sum(L[i:j]) > s:
            s=sum(L[i:j])
            c=L[i:j]
    return s,c
    

print maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        
