class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adj = collections.defaultdict(set)
        que=[]
        if n == 1:
            return [0]
        
        
        for x,y in edges:
            adj[x].add(y)
            adj[y].add(x)
            
        que=[i for i in range(n) if len(adj[i])==1]
        
        while n>2:
            n -= len(que)
            newque=[]
            for x in que:
                print(x)
                for y in adj[x]:
                    adj[y].remove(x)
                    if len(adj[y])==1:
                        newque.append(y)
                
            que = newque
                
                
        return que
            
        
        
                    
        
    
                
            
            
            
             
        
