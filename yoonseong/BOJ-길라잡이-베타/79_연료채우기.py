import sys
import heapq

N = int(sys.stdin.readline())

gas = []

for i in range(N):
    # a: 시작 지점부터 주유소까지의 거리 b: 주유소에 있는 기름
    a, b = map(int, sys.stdin.readline().split())
    gas.append((a, b))

gas.sort()  # 주유소를 가까운 거리순으로 정렬

# L: 시작 지점부터 마을까지의 거리 P: 차에 있는 기름
L, P = map(int, sys.stdin.readline().split())

move = []
answer = 0


while P < L:  # 처음부터 기름이 충분하면 반복x
    while gas and gas[0][0] <= P:  # 현재 기름으로 갈 수 있는 주유소
        fuel = heapq.heappop(gas)[1]
        # 넣을 수 있는 기름이 가장 많은 곳을 내림차순되게 heap에 push (최대힙)
        heapq.heappush(move, -fuel)

    if not move:  # 현재 기름으로 다음 주유소에 갈 수 없다면 -1
        answer = -1
        break

    fuel = heapq.heappop(move)  # 가장 연료가 많은 주유소의 기름을 pop

    P += -fuel  # 가지고 있는 연료에 더해줌
    answer += 1

print(answer)
