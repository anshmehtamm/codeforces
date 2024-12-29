
t = int(input())
# global m
m = 0

def recurse(l,r,k):
    global m
    x = (l+r)//2
    n = r-l+1

    if n<k:
        return
    if n%2==1:
        m += x
        recurse(l,x-1,k)
        recurse(x+1,r,k)
    else:
        # even
        # recursion is also even
        if k==1:
            m+= (n*(n+1))//2
            return
        else:
            recurse(l,x,k)
            recurse(x+1,r,k)


for _ in range(t):
    n,k = map(int, input().split())
    m = 0

    if n%2==0 and k==1:
        print(n*(n+1)//2)
        continue

    recurse(1,n,k)
    print(m)

