import sys

sides = []

num_cells = int(sys.stdin.readline())
data = sys.stdin.readline()

scores = [int (n) for n in data.split()]

total_score = scores[0]
for i in range(1,num_cells-1):
    if scores[i] > 0:
        total_score += scores[i]

total_score += scores[num_cells-1]

print(total_score)
    

