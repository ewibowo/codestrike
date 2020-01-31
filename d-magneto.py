import sys

def main():
    num_jars = sys.stdin.readline()
    data = sys.stdin.readline()
    parents = [int (n) for n in data.split()]

    jars = dict()
    
    total_step = 0

    i = 2
    for p in parents:
        jars[i] = p
        i += 1
   
    for j in jars.keys():
        curr_parent = jars[j]
        total_step += 1
        while (curr_parent != 1):
            curr_parent = jars.get(curr_parent)
            total_step += 1
            
    print(total_step)

if __name__ == "__main__":
    main()
