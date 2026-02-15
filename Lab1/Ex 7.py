n=int(input("n= "))
while not (n>2):
    n=int(input("n= "))
ch=str(n)
s=0
for i in range(len(ch)):
    s+=int(ch[i])
if n%s==0:
    print("niven number")
else:
    print("NOT a niven number")