def input_number():
    global x
    while True:
        try:
            x=int(input("x= "))
            if x>0:
                break
        except: continue
    
def reverse_number(x):
    y=0
    while x>0:
        dig=x%10
        y=y*10+dig
        x//=10
    print(y)

input_number()
reverse_number(x)
