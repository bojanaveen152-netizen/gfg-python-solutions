def final_fun(arg):
    if arg == 1:
        result="One"
    elif arg==2:
        result="Two"
    elif arg==3:
        result="Three"
    elif arg==4:
        result="Four"
    elif arg==5:
        result="Five"
    elif arg==6:
        result="Six"
    elif arg==7:
        result="Seven"
    elif arg==8:
        result="Eight"
    elif arg==9:
        result="Nine"
    else:
        result="Unknown"
    
    return result 

n=int(input())
result=final_fun(arg=n)
print(result)
