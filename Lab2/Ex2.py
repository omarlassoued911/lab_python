def input_number():
    global x
    while True:
        try:
            x=int(input("x= "))
            if x>0:
                break
        except: continue

def is_perfect(x):
    s=0
    for i in range(1,(x//2)+1):
        if x%i==0:
            s+=i
    return s==x

def display_perfect_number(maxn):
    first=True
    for i in range(1,maxn+1):
        if is_perfect(i):
            if first:
                print(end="")
                first=False
            else:
                print(end="|")
            print(i,end="")
            
            
input_number()
maxn=int(input("maxn= "))
if is_perfect(x):
    print(x," is perfect")
else:
    print(x," is not perfect")
display_perfect_number(maxn)
    