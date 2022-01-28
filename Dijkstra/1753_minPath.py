import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict

V, E = map(int, input().split())
K = int(input())
graph = defaultdict(list) #c++의 vector 같다 ..
INF = sys.maxsize
dp = [INF] * (V+1)
queue = []

def dijkstr(start):
    heapq.heappush(queue, (0, start))
    while queue:
        dist, now = heapq.heappop(queue)
        #dp에 저장된 값이 더 적어 최소 비용이 이미 계산되었을 경우 무시
        if dp[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[1]
            if cost < dp[node[0]]:
                dp[node[0]] = cost
                heapq.heappush(queue, (cost, node[0]))

    dp[start] = 0


for _ in range(E):
    s, e, v = map(int, input().split())
    graph[s].append((e, v))


dijkstr(K)
for i in range(1, V+1):
    print("INF" if dp[i] == INF else dp[i])

