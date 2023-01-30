import sys

input = sys.stdin.readline

word_front = list(input().strip())
word_back = []

m = int(input())
cursor = len(word_front)

for _ in range(m):
    tmp = input().strip()
    if tmp[0] == "P":
        word_front.append(tmp[2])
        cursor+=1
    elif tmp == "L":
        if cursor != 0:
            cursor -= 1
            word_back.append(word_front.pop())
    elif tmp == "D":
        if cursor != len(word_front)+len(word_back):
            cursor += 1
            word_front.append(word_back.pop())
    else:
        if cursor != 0:
            word_front.pop()
            cursor -= 1

print("".join(word_front)+"".join(word_back[::-1]))

# import sys    # 시간초과

# input = sys.stdin.readline

# word = list(input().strip())
# m = int(input())
# cursor = len(word)

# for _ in range(m):
#     tmp = input().strip()
#     if " " in tmp:
#         word.insert(cursor, tmp[2:])
#         cursor+=1
#     elif tmp == "L":
#         if cursor != 0:
#             cursor -= 1
#     elif tmp == "D":
#         if cursor != len(word):
#             cursor += 1
#     else:
#         if cursor != 0:
#             word.pop(cursor-1)
#             cursor -= 1

# print("".join(word))