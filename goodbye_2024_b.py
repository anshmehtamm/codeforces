t = int(input())

for _ in range(t):
    n = int(input())
    a = []
    cannot = [0 for i in range(2*n+1)]
    for i in range(n):
        a.append(list(map(int, input().split())))
        if a[i][0] == a[i][1]:
            cannot[(a[i][0])] += 1

    prefix_cannot = [0 for i in range(2*n+1)]
    for i in range(1,2*n+1):
        if cannot[i]>=1:
            prefix_cannot[i] = prefix_cannot[i-1] + 1
        else:
            prefix_cannot[i] = prefix_cannot[i-1]
    ans = []
    for i in range(n):
        if a[i][0] == a[i][1] and cannot[a[i][0]] > 1:
            ans.append(0)
        elif a[i][0] == a[i][1] and cannot[a[i][0]] == 1:
            ans.append(1)
        else:
            l = a[i][0]
            r = a[i][1]
            numbers_left = prefix_cannot[r]-prefix_cannot[l-1]
            if (r-l+1)>numbers_left:
                ans.append(1)
            else:
                ans.append(0)

    print(''.join(map(str,ans)))



