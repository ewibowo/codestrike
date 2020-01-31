import sys

sides = []

data = sys.stdin.readline()

sides = [int (n) for n in data.split()]

for side in sides:
    if (side<1 or side>100):
        exit(1)

sides.sort()

if (sides[2]) < (sides[0]+sides[1]):
    print(0)
else:
    print((sides[2]-(sides[0]+sides[1]))+1)
