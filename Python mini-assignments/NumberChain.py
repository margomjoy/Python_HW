
rn="y"
vect=[]

ent=int(input("How many numbers? "))
for x in range(ent):
    print(x)
    

z=(x+1)

while rn=="y":
    rn=input("Continue the chain: (y)es or (n)o? ")  
    if rn=="n":
        break
    
    ent2=int(input("How many numbers? "))    
    for y in range(z,(z+ent2)):
        print(y)
       

