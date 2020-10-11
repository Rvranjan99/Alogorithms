def isSubset(a,n,sum):
    dp=[[0 for i in range(sum+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    for i in range(sum+1):
        dp[0][i]=False
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if j<a[i-1]:
                dp[i][j]=dp[i-1][j]
            if j>=a[i-1]:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-a[i-1]]
    return dp[n][sum]
    
    
a=[1,4,6,8]
sum1=10
sum2=11
if isSubset(a,len(a),sum1)==True:
    print("subset is found")
else:
    print("No subset is found")
    
if isSubset(a,len(a),sum2)==True:
    print("subset is found")
else:
    print("No subset is found")
