def input_number():
    
    while True:
        try:
            x=int(input("Enter a number: "))
            if 100<=x<=999:
                break
        except ValueError:
            print("Invalid input. Please enter a 3 digits number.")
    return x

def armstrong(x):
    return x/100**3 + (x%100//10)**3 + (x%10)**3 == x

def est_armstrong(x):
    for i in range(100,999):
        if armstrong(i):
            print(i)

x=input_number()
est_armstrong(x)