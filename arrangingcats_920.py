t = int(input())

for i in range(t):
    n = int(input())
    original = input()
    arranged = input()
    p1 = 0
    p2 = 0
    for j in range(n):
        if original[j] == arranged[j]:
            continue
        elif original[j] == '0' and arranged[j] == '1':
            p1 += 1
        else:
            p2 += 1
    ans = 0
    diff = min(p1,p2)
    ans += diff
    p1 -= diff
    p2 -= diff
    ans += max(0,p1)
    ans += max(0,p2)
    print(ans)



