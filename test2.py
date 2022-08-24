import sys
r=sys.stdin.readline
N=int(r())
food=list(map(int,r().split()))
dp=[0] * 101
dp[0]=food[0]
dp[1]=food[1]
for i in range(2,N):
	dp[i] = max(dp[i-1], dp[i-2]+food[i])
print(dp[N-1])