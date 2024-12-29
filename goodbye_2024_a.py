t = int(input())

for _ in range(t):


    n = int(input())
    a = list(map(int, input().split()))

    if n==1:
        print("YES")
        continue

    found = False
    for i in range(n-1):
        x = a[i]
        y = a[i+1]

        if ((x+y)>y) and ((y+x)>x) and (x+x>y) and (y+y>x):
            found=True
            break
    if found:
        print("YES")
    else:
        print("NO")
