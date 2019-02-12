#Ergasia 3
#Antonis Ekatommatis
#Eisagwgh sthn episthmh twn ypologistwn
#1o Eksamino

#Anoigma arxeiou gia Read
fin=open("hello_world.py","r")
#apothikeusi sthn metavliti lines oles tis grammes tou kwdika
lines=fin.readlines()
fin.close()
#Kleisimo arxeiou

#Anoigma arxiou gia Write
fin = open("hello_world.py","w")

final_list=[]

for line in lines:
    counter1=0
    counter2=0
    if "#" in line:
        y=list(line)
        x=y.index("#")
        for i in range(x,0,-1):
            if line[i] == "'":
                counter1+=1
            elif line[i] == '"':
                counter2+=1
        if counter1 % 2 == 1 or counter2 % 2 == 1:
            final_list.append(line)
        else:
            for i in range(0,x):
                final_list.append(y[i])
        if line[0] != "#":
            final_list.append("\n")
    else:
        final_list.append(line)
        
final="".join(final_list)
fin.write(final)
    
fin.close()
