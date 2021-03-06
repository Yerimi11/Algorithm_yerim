import sys
sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/문자열&1,2차원리스트탐색/11. 격자판 회문수/in5.txt", 'r')

G = [list(map(int, input().split())) for _ in range(7)]

# 가로 탐색, 세로 탐색 한 줄 씩 리스트에 넣고, 5자리 회문 발견하면 cnt += 1
# 회문 확인 방법은 3cases가 있다. OOOOOXX, XOOOOOX, XXOOOOO
# 출발 인덱스 [0],[4] / [1],[5] / [2],[6] 를 검사하면 된다. [i], [i+4]
#  ㄴ 같으면 [j+1], [j-1] 이렇게 줄여나가며 회문인지 검사한다.

cnt = 0
temp = []

for ix in range(7):
    for jx in range(7):
        temp.append(G[ix][jx]) # 가로줄 1줄씩 넣음
    for x in range(3):         # 회문 검사
        if temp[x] == temp[x+4]:
            if temp[x+1] == temp[x+3]:
                cnt += 1
    temp = []

for iy in range(7):
    for jy in range(7):
        temp.append(G[jy][iy])  # 세로줄 1줄씩 넣음
    for x in range(3):          # 회문 검사
        if temp[x] == temp[x+4]:   
            if temp[x+1] == temp[x+3]:
                cnt += 1
    temp = []

print(cnt)

# 회문 탐색 시 슬라이싱을 이용하는 방법도 있다!
# for i in range(3):
#     for j in range(7):
#         temp = G[j][i:i+5]
#         if temp == temp[::-1]:
#             cnt += 1
#         for k in range(2): # 세로줄 위, 아래 좁혀가며 회문 확인
#             if G[i+k][j] != G[i+5-k-1][j]:
#                 break
#         else:
#             cnt+=1
        
# print(cnt)


# 또는
# for i in range(7): #행, 열
#     start = 0
#     for _ in range(3):
        
#         if G[i][start]==G[i][start+4] and G[i][start+1]==G[i][start+3]:
#             cnt+=1
#         if G[start][i]==G[start+4][i] and G[start+1][i]==G[start+3][i]:
#             cnt+=1
            
#         start+=1
#         if start ==3:
#             break

# print(cnt)