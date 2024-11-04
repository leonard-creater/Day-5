def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
    
num=int(input("enter value"))

if num <0:
    print("no fatorial number")

elif num ==0:
    print("factorial number")

else:
    print("factorial number is",num)
     
fact(num)