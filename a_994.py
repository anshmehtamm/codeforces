t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mid = False
    for i in range(1,n-1):
        if a[i]==0:
            mid = True
            break

    all0 = True
    # check if all 0s
    for i in range(n):
        if a[i]!=0:
            all0 = False
            break

    if all0:
        print(0)
        continue

    if mid==True and a[0]==0 and a[-1]==0:
        print(2)
        continue

    if mid==True and a[0]==0:
        print(1)
        continue

    if mid==True and a[-1]==0:
        print(1)
        continue

    if mid==True:
        print(2)
        continue

    if mid==False:
        print(1)
        continue