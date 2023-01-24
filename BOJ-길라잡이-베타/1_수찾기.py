N = int(input())
data_N = list(map(int, input().split()))
data_N.sort()

M = int(input())
data_M = list(map(int, input().split()))

def binary_search(arr, item, start, end):
  while start <= end:
    mid = (start + end)//2

    if arr[mid] == item:
      return 1
    elif arr[mid] < item:
      start = mid + 1
    else:
      end = mid - 1

  return 0

for m in data_M:
  print(binary_search(data_N, m, 0 , N-1))
