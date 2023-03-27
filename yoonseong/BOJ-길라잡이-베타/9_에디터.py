import sys

text = list(input())
temp_text = []

N = int(input())

for _ in range(N):
  data = sys.stdin.readline().split()

  if data[0] == 'L':
    if len(text) > 0:
      temp_text.append(text.pop())
  elif data[0] == 'D':
    if len(temp_text) > 0:
      text.append(temp_text.pop())
  elif data[0] == 'B':
    if len(text) > 0:
      text.pop()
  elif data[0] == 'P':
    text.append(data[1])

reverse_temp_text = list(reversed(temp_text))
print("".join(text + reverse_temp_text))

# 시간초과. append와 pop이 insert, del보다 빠름
# import sys

# text = list(input())

# N = int(input())

# cursor = len(text)

# for _ in range(N):
#   data = sys.stdin.readline().split()

#   if data[0] == 'L':
#     if cursor > 0:
#       cursor -= 1
#   elif data[0] == 'D':
#     if cursor < len(text) + 1:
#       cursor += 1
#   elif data[0] == 'B':
#     if cursor > 0:
#       del (text[cursor-1])
#       cursor -= 1
#   elif data[0] == 'P':
#     text.insert(cursor, data[1])
#     cursor += 1

# print("".join(text))
