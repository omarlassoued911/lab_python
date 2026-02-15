def palindrome_recur(ch):
    if len(ch)==1 or len(ch)==0:
        return True 
    
    elif ch[0]!=ch[-1]:
        return False
    else:
        return palindrome_recur(ch[1:len(ch)-1])

print(palindrome_recur("radar"))