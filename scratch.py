t = int(input())

for test in range(t):

    n,m,L = map(int,input().split())
    hurdles = []
    powerups = {}
    for i in range(n):
        l,r = map(int,input().split())
        hurdles.append((l,r))
    for i in range(m):
        x,y = map(int,input().split())
        if x not in powerups:
            powerups[x] = []
        powerups[x].append(y)

    # convert powerups to sorted list (x,[y1,y2,y3])
    powerups_list = []
    for x in sorted(powerups.keys()):
        powerups_list.append((x,powerups[x]))

    min_powerups_to_use = 0

    current_total = 1
    powerups_index = 0
    unused_powerups = []
    cannot_pass = False
    # for all hurdles we will check if it can be passed with current powerups
    for hurdle in hurdles:
        l,r = hurdle
        req = (r-l+2)
        can_pickup = []
        while powerups_index < len(powerups_list):
            pos = powerups_list[powerups_index][0]
            if pos<l:
                #flatten
                for y in powerups_list[powerups_index][1]:
                    can_pickup.append(y)
            else:
                break
            powerups_index += 1

        can_pickup.sort(reverse=True)
        # check which powerups can be used
        for i in range(len(can_pickup)):
            if current_total<req:
                current_total += can_pickup[i]
                min_powerups_to_use += 1
                can_pickup[i] = -1
            else:
                break;
        # add to unused powerups
        #print(req, current_total, can_pickup, unused_powerups, min_powerups_to_use)
        for i in range(len(can_pickup)):
            if can_pickup[i] != -1:
                unused_powerups.append(can_pickup[i])
        # if we still can't pass the hurdle
        if current_total<req:
            # check unused powerups
            unused_powerups.sort(reverse=True)
            for i in range(len(unused_powerups)):
                if current_total<req:
                    if unused_powerups[i] == -1:
                        continue
                    current_total += unused_powerups[i]
                    min_powerups_to_use += 1
                    unused_powerups[i] = -1
                else:
                    break

        if current_total<req:
            cannot_pass = True
            break

    if cannot_pass:
        print(-1)
    else:
        print(min_powerups_to_use)











