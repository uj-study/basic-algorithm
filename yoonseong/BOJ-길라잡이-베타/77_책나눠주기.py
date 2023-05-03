import sys

T = int(sys.stdin.readline())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split()) # N : 책의 권 수 M : 학부생 수
    application_num = [] # 신청 책 번호 배열
    books = [False for _ in range(N + 1)] # 책 목록
    answer = 0
    
    for j in range(M):
        a, b = map(int, sys.stdin.readline().split())
        application_num.append((a, b))

    # 원하는 책의 끝 번호를 기준으로 오름차순 정렬
    application_num.sort(key=lambda a : a[1])
  
    for a in application_num:
        for k in range(a[0], a[1]+1): # 원하는 번호 범위를 돌면서
          if not books[k]: # 아직 남아있는 책이면
            answer += 1
            books[k] = True # 책이 없음으로 체크
            break
    print(answer)
