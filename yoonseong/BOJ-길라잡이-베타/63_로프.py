import sys

N = int(sys.stdin.readline())
ropes = []

for i in range(N):
    ropes.append(int(sys.stdin.readline()))

ropes.sort(reverse=True)

answer = []

for i in range(N):
    answer.append((i+1) * ropes[i])

print(max(answer))

# for r in ropes:
#     count += 1

#     if count * r >= answer:
#         answer = count * r
#     else:
#         count -= 1
