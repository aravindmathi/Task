#-----------------------------------------------------------------------------------------------------
#Question 0
alp="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
try:
    s=int(input("#size "))
    if s>52:
        raise IndexError    
    middle,cnt=((4*(s-1))+1)//2,0

    for total in range(s*2-1):
        print() 
        start,end,mark=middle-2*cnt,middle+2*cnt,0
        for line in range((4*(s-1))+1):
            if line%2 ==0 and line>=start and start<end+1:                
                if line<=middle:                    
                    print(alp[s-1+mark],end="")
                    mark-=1                    
                    #start+=2                    
                elif line>middle:                    
                    print(alp[s+1+mark],end="")
                    mark+=1
                start+=2   
            else:
                print("-",end="")        
        if total <(s*2-1)//2:
            cnt+=1
        else:
            cnt-=1
except IndexError:
    print("Please enter number < 53")
except:
    print("Please enter a number")

print()
#-------------------------------------------------------------------------------------------------------
#Question 1
#Raise exception if the given input is not number
try:
    n=int(input("n = "))
#Determine the first and last number
    cnt,first,last=n,1,n*(n+1)
    for i in range(n):
        print()
        print("*"*2*(n-cnt),end="")
        for j in range(first,first+cnt):
            print(str(j)+'0',end='')
        for k in range(last-cnt+1,last+1):
            if k!=last:
                print(str(k)+'0',end='')
            else:
                print(str(k),end='')
#First and last number of each line
        first=first+cnt
        last=last-cnt
        cnt-=1
except:
    print("Please enter a number")

print()
#------------------------------------------------------------------------------------------------------
#Question2
#Fibonacci with recursion
def Fibonacci(n):
    if n<=1:
        return n
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
n=int(input("n ")
print(Fibonacci(n))


