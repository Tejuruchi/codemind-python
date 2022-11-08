def prime(num):
    if(num==1):
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if(num%i==0):
                return False
    return True
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if(prime(i)):
        c+=1
print(c)