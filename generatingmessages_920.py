t = int(input())
for _ in range(t):
    inputString = input()

    lastCap = []
    lastLow = []
    removal = set()
    for i in range(len(inputString)):
        if inputString[i]=='b':
            removal.add(i)
            if len(lastLow)>0:
                removal.add(lastLow[len(lastLow)-1])
                del lastLow[-1]
        elif inputString[i]=='B':
            removal.add(i)
            if len(lastCap)>0:
                removal.add(lastCap[len(lastCap)-1])
                del lastCap[-1]
        else:
            if (inputString[i].isupper()):
                lastCap.append(i)
            if (inputString[i].islower()):
                lastLow.append(i)

    for i in range(len(inputString)):
        if (i in removal):
            continue
        print(inputString[i], sep='', end='')
    print('')
