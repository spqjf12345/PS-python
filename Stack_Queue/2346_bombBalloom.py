import sys
num = int(sys.stdin.readline())
index = [i for i in range(1, num + 1)]
queue = list(map(int, input().split()))
initial = queue[0]
queue.pop(0)
print(index.pop(0), end= ' ')
idx = 0

while queue:
    if(initial > 0): #양수라면
        idx = (idx + (initial-1)) % len(queue)
    else:
        idx = (idx + initial) % len(queue) # 왼쪽 방향
    initial = queue.pop(idx)
    print(index.pop(idx), end= ' ')


