class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp=[[0]*(n+1) for i in range(m+1)]
        for di,dj in [count(s) for s in strs]:
            for i in reversed(range(0,m+1)):
                for j in reversed(range(0,n+1)):
                    if i>=di and j>= dj:
                        dp[i][j]=max(dp[i-di][j-dj]+1,dp[i][j])
                        
        return dp[-1][-1]
            
        
     
def count(strs):
    x='0'
    y='1'
    x_0=strs.count(x,0,len(strs))
    y_1=strs.count(y,0,len(strs))
    return x_0,y_1
    
    
        
