def input_number():
    global x,y
    while True:
        try:
            x=int(input("x= "))
            if x>0:
                break
        except: continue
    while True:
        try:
            y=int(input("y= "))
            if y>0:
                break
        except: continue

def gcd(x,y):
    if x==y:
        return x
    elif x>y:
        return gcd(x-y,y)
    else:
        return gcd(x,y-x)

input_number()
print("the gcd of ",x," and ",y," is ",gcd(x,y))