def solve():
    import sys
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()

        # Find p_max and s_min
        p_max = 0
        s_min = n + 1
        for i, ch in enumerate(s, 1):
            if ch == 'p':
                p_max = max(p_max, i)
            elif ch == 's':
                s_min = min(s_min, i)

        # Check cases
        if p_max == 0 and s_min == n+1:
            # No 'p' and no 's' constraints
            print("YES")
        elif p_max == 0:
            # No 'p' constraints, possibly 's' constraints only
            print("YES")
        elif s_min == n+1:
            # No 's' constraints, only 'p' constraints
            print("YES")
        else:
            # Both 'p' and 's' constraints
            if p_max < s_min:
                # No overlap
                print("NO")
            else:
                # There is overlap
                overlap = p_max - s_min + 1
                intersection_size = min(p_max, n - s_min + 1)
                if overlap >= intersection_size:
                    print("YES")
                else:
                    print("NO")

if __name__ == "__main__":
    solve()
