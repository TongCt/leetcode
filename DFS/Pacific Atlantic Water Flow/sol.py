class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        result = []
        m = len(matrix)
        n = len(matrix[0])
        Pacific = [[False for i in range(n)] for i in range(m)]
        Atlantic = [[False for i in range(n)] for i in range(m)]
        INT=0
        for i in range(m):
            dfs(matrix,Pacific,INT,i,0)
            dfs(matrix,Atlantic,INT,i,n-1)
        for i in range(n):
            dfs(matrix,Pacific,INT,0,i)
            dfs(matrix,Atlantic,INT,m-1,i)
            
        for i in range(m):
            for j in range(n):
                if(Pacific[i][j] and Atlantic[i][j]):
                    result.append([i,j])

        return result
        
        
def dfs(matrix,visit,pre,i,j):
    m = len(matrix)
    n = len(matrix[0])
    if(i>=m or i<0 or j<0 or j>=n or matrix[i][j]<pre or visit[i][j]):
        return
 
    visit[i][j] = True
    dfs(matrix,visit,matrix[i][j],i+1,j)
    dfs(matrix,visit,matrix[i][j],i,j+1)
    dfs(matrix,visit,matrix[i][j],i-1,j)
    dfs(matrix,visit,matrix[i][j],i,j-1)
    
    
    
