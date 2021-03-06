import sys
input = sys.stdin.readline


def binary(n_list, target):
    left, right = 0, n-1

    while left <= right:
        mid = (left+right) // 2
        # for i in range(len(m_list)): # m_list의 숫자가 n_list에 있는지 이분탐색으로 조사하기
        if n_list[mid] == target:
            return 1
        elif n_list[mid] < target:
            left = mid + 1
        else: 
            # n_list[mid] > target:
            right = mid - 1
    return 0

n = int(input())
n_list = list(map(int, input().split())) # 이걸 이분탐색 해야하지?
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort() # 1 2 3 4 5

for i in range(len(m_list)):
    print(binary(n_list, m_list[i]))



# import sys
# input = sys.stdin.readline
# n = int(input())
# n_list = list(map(int, input().split())) # 이걸 이분탐색 해야하지?
# m = int(input())
# m_list = list(map(int, input().split()))

# n_list.sort() # 1 2 3 4 5

# left, right = 0, n

# while left <= right:

#     mid = (left+right) // 2
#     for i in range(len(m_list)): # m_list의 숫자가 n_list에 있는지 이분탐색으로 조사하기
#         if n_list[mid] == m_list[i]:
#             print('1')
#         elif n_list[mid] < m_list[i]:
#             left = mid + 1
#         elif n_list[mid] > m_list[i]:
#             right = mid - 1
#         else:
#             print('0')

            
