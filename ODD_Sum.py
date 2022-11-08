n=int(input())
lst=list(map(int,input().split()))
odds=[i for i in lst if i %2!=0]
print(sum(odds))