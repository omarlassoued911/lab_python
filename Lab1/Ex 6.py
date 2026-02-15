n=int(input("n= "))
while not (n>2):
    n=int(input("n= "))

ch=str(n)
ch1=""
for i in range(len(ch)):
    ch1=ch[i]+ch1
if ch==ch1:
    print(n," is palindrome number")
else:
    print(n," is  not palindrome number")