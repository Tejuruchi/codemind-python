for kfjdkf in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    i=0
    ansl=0
    while i<n:
        mn=b[i]
        mx=b[i]
        for j in range(i,n+1):
            mx=max(mx,a[j])
            if mx==b[j]:
                ansl+=mx-mn
                i=j+1
                break
    print(ansl)