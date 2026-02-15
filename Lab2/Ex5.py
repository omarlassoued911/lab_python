def input_recur():
    global x
    x=int(input("x= "))
    if x<=0:
        input_recur()
    else:
        return x

def div_recur(a, b):
    if a==0:
        return True
    elif a<b:
        return False
    else:
        return div_recur(a-b,b)

def quo_recur(a, b):
    if a<b:
        return 0
    else:
        return 1+quo_recur(a-b,b)
    


x=input_recur()
print(div_recur(10, 5))
print(quo_recur(20, 5))
