def list_to_9_recur(N):
    ch="["
    n=N
    while (n!=9):
        x=(n%10)*10+n//10
        ch+=str(n)+","+str(x)+","
        n=abs(n-x)
    print(ch+"9]")
        
list_to_9_recur(63)