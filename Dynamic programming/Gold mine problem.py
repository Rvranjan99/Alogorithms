def maxGold(gold,m,n):
    gold_table=[[0 for i in range(m)] for j in range(n)]
    
    
    for col in range(n-1,-1,-1):
        for row in range(m):
            #right with corner case
            if col==n-1:
                right=0
            else:
                right=gold_table[row][col+1]
            #right up with corner case
            if row==0 or col==n-1:
                right_up=0
            else:
                right_up=gold_table[row-1][col+1]
            #right down with corner case
            if row==m-1 or col==n-1:
                right_down=0
            else:
                right_down=gold_table[row+1][col+1]
            #updating the table with max(all possible move)
            gold_table[row][col]=gold[row][col]+max(right,right_up,right_down)
            
    #since initially miner can start from col0 and any row, hence we choose max
    ans=gold_table[0][0]
    for i in range(1,m):
        ans=max(ans,gold_table[i][0])
    return ans



gold = [[1, 3, 1, 5], 
    [2, 2, 4, 1], 
    [5, 0, 2, 3], 
    [0, 6, 1, 2]]
m=4
n=4
print(maxGold(gold,m,n))
