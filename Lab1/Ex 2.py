ch=str(input("ch= "))
nb=0
for i in range (len(ch)):
    if ch[i] in ["A","a","E","e","I","i","O","o","U","u"]:
        nb+=1
print (nb)