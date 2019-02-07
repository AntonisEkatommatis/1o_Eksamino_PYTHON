#Ergasia 3
#Antonis Ekatommatis
#Eisagwgh sthn episthmh twn ypologistwn
#1o Eksamino
fin=open("hello_world.py","r")
lines=fin.readlines()
fin.close()

fin = open("hello_world.py","w")
for line in lines:
    if line[0] != "#":
        fin.write(line)
fin.close()
