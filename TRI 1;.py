tab=[15,30,-2,6,-15]
for i in range(5):
    min=tab[i]
    for j in range(i,5):
        if min>tab[j]:
            min=tab[j]
            tab[j]=tab[i]
            tab[i]=min
print(tab)