import sys

N = int(input())
words = []

for _ in range(N):
  word = sys.stdin.readline().rstrip()
  words.append(word)

removeDuplicate = list(set(words))
removeDuplicate.sort() # 사전순으로 정렬 후
removeDuplicate.sort(key=len) # 길이로 정렬


for word in removeDuplicate:
  print(word)