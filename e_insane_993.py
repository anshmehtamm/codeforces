def ceil(x):
  return -int(-x // 1)

import math
t = int(input())
for _ in range(t):
    k, l1, r1, l2, r2 = map(int, input().split())
    # y = k^n * x
    ans = 0
    n = 0
    while n<=32:
        z = k**n
        # find bound of l2, r2
        y_l = z*l1
        y_r = z*r1
        # both are outside
        if (y_l<l2 and y_r<l2) or (y_l>r2 and y_r>r2):
            pass
        maxx = max(l1,ceil(l2/z))
        minn = min(r1,r2//z)
        if maxx<=minn:
            ans+=(minn-maxx+1)
        n += 1
    print(ans)
