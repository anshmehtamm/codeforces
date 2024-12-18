def square():
    t = int(input())
    for i in range(t):
        sidesX = []
        sidesY = []
        for j in range(4):
            x,y = map(int,input().split())
            sidesY.append(y)
            sidesX.append(x)
        lefx = min(sidesX)
        rightx = max(sidesX)
        lefy = min(sidesY)
        righty = max(sidesY)
        print((righty-lefy)*(rightx-lefx))
if __name__ == '__main__':
    square()

