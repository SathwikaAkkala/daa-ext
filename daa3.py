#dynamaic 0-1 kanpsack(v,w,n,W)
#for w =0 to W do
#c[0,w]=0
#for i=1 to n do
#c[i,0]=0
#for w=1 to W do
#if wi<=w then
#if vi+c[i-1,w-wi] then
#c[i,w]=vi+c[i-1,w-wi]
#else
#c[i,w]=c[i-1,w]
#else
#c[i,w]=c[i-1,w]
def knapsack(weights,values,capacity):
    n=len(weights)
    dp=[[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,capacity+1):
            if weights[i-1]<=w:
                dp[i][w]=max(dp[i-1][w],dp[i-1][w-weights[i-1]]+values[i-1])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][capacity]
n=int(input("enter the number of items:"))
weights=list(map(int,input("enter the no of weights:").split()))
values=list(map(int,input("enter the no of values:").split()))
capacity=int(input("enter the kanpsack capacity:"))
print("max value:",knapsack(weights,values,capacity))

             









