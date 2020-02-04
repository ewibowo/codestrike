'''First section is to create V and for testing only'''
import sys

line1 = sys.stdin.readline()
#N, K = [int(n) for n in line1.split()]
N, K = map(int, line1.split())

line2 = sys.stdin.readline()
V = [int(n) for n in line2.split()]

V.sort()

difference = []
smallestvalue = 1000000000

'''V is now sorted. The first step is to go through each possible variation of V
with K integers removed.

For example a sorted V would look like this:
V = [-3, -2, 3, 6, 8]

and if K = 2
Vnew will run through the following variations:
    [-3, -2, 3]
        [-2, 3, 6]
            [3, 6, 8]
'''


for j in range(0,K+1):
    Vnew = V[j:N-(K-j)]
    for i in range(len(Vnew)-1):
        difference.append(Vnew[i+1]-Vnew[i])
    M = Vnew[N-K-1]-Vnew[0]
    m = min(difference)
    if smallestvalue >= M+m:
        smallestvalue = M+m
    difference = []

'''
To get M, it will always be the difference first and last numbers of Vnew
(where Vnew = V without K integers)

To get m, you take the smallest difference - which is why there's a difference
list. The difference list takes in all the differences between a number and the
number after it in Vnew.

For example:
Vnew =      [-3, -2, 3]
difference =   [1 , 5]
M = 3 - (-3) -> 6
m = min(difference) -> 1

'''


'''
The smallestvalue is compared and then goes back to for loop to try another Vnew
'''

print(smallestvalue)
