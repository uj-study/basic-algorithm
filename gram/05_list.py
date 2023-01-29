a = [1, 2, 3, 4, 5, 4]
a.append(4)             # 마지막 인덱스에 4 추가
a.extend([5, 6, 7])     # 마지막 인덱스부터 배열 연결
a.remove(4)             # 가장 빠른 인덱스에서 해당 값 찾아서 삭제
a.pop()                 # 마지막 인덱스 삭제
a.pop(2)                # 인덱스 2의 값 삭제

a[0:3]                  # 0~2번째 인덱스 출력
a[0:3:2]                # 0~2번째 인덱스 2개씩 건너뛰며 출력
a[:2]                   # 앞에서 2개 출력
a[2:]                   # 앞에서 2개 빼고 출력
a[::2]                  # 앞에서부터 2개씩 건너뛰며 출력
a[::-1]                 # 역순으로 출력
a[-1]                   # 마지막 인덱스 값 출력

if a: '배열 a가 비어있지 않다면 실행'
else: '배열 a가 비어있다면 실행'

if a[0]: 'a의 0 번째 인덱스가 0이 아니라면 실행'
else: 'a의 0 번째 인덱스가 0이라면 실행'

b = (1, 2, 3)           # 튜플은 데이터 변경 불가
c = 1, 2, 3
print(b[1])
print(c[1])

d = {1, 2, 3, 2}        # 세트는 인덱스 개념 없고 중복 불가능
print(d)                # {1, 2, 3}
                        # 출력시 자동 정렬상태.

e = {'a': 1, 'b': 2, 'c': 3}
print(e['b'])

a = [int(x) for x in input().split()]  # 가 반복돌며 리스트에 들어감

import sys  
a = list(map(int, input().split()))

f = [1, 3, 2]
f.sort(reverse=True)

list2 = [(1, 2), (1, 3), (2, 2)]

# 아래 두가지 방법으로 튜플의 첫 값으로 정렬 후 같을 시 두번째 값으로 다시 정렬
list2.sort(key=lambda x: (x[0], x[1]))

result = sorted(list2)

p = list('abcd')        # ['a', 'b', 'c', 'd']
print(*p)               # a b c
print(*p, sep='\n')     # a
                        # b
                        # c

def sol(a):
    return
na = 4
a[1, 2, 3, 4, 5, 6]             # 앞 뒤 빼가며 반복시키며 함수 대입 시행 가능
sol([i[:na] for i in a[:na]])
sol([i[na:] for i in a[:na]])

# 리스트를 복사할 때, a = b 로 하면 주소 복사하여 수정시 다같이 수정됨
b = []
a = b[:]
a = b.copy()    # 가독성이 좋은 범용적 사용
a = list(b)
a = [] + b