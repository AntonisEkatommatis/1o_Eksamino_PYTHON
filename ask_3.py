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

for line in lines:
    if "#" in line:
        y=list(line)
        x=y.index("#")
        for i in range(0,x):
            final_list.append(y[i])
        if line[0] != "#":
            final_list.append("\n")
    else:
        final_list.append(line)
        
final="".join(final_list)
fin.write(final)
    
fin.close()
