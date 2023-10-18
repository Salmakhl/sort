tab=[]
n=int(input("entrer la taille:"))
for t in range(n):
    b=int(input("veuillez tapez un nombre: "))
    tab.append(b)
for i in range(0,n):
    min=tab[i]
    for j in range(i,n):
        if min>tab[j]:
            min=tab[j]
            tab[j]=tab[i]
            tab[i]=min    
print(tab)