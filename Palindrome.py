def rev(n):
    sum=0
    while n>0:
        rem=n%10
        sum=sum*10+rem
        n=n//10
    return sum
a=int(input())
if a==rev(a):
    print("True")
else:
    print("False")