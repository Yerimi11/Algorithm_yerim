import sys
sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/완전탐색,DFS기초/8. 순열 구하기/in5.txt", "r")
input = sys.stdin.readline

def DFS(L):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end = ' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if check[i] == 0:
                check[i] = 1
                res[L] = i
                DFS(L+1)
                check[i] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    # lst = list(range(1, n+1))
    cnt = 0
    res = [0] * m
    check = [0] * (n+1)
    DFS(0)
    print(cnt)