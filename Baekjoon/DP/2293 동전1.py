# https://www.acmicpc.net/problem/2293
# 1. dp테이블은 n개가 아니라, 동전을 최대로 가질 수 있는 갯수를 만든다.
# coin,i를 이용해 2차원 dp를 구현할 때는, coin고정 & i만 dp기록 하는 식으로 움직인다
# bfs, dp
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k+1)]
dp[0] = 1

for coin in coins:
    for i in range(coin, k+1):
        if i-coin >= 0:
            dp[i] += dp[i-coin] # 경우의 수 갯수를 기록

print(dp[k])

