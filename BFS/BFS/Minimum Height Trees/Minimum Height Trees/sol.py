
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
            
       ##这道题很难说是BFS， 像是拓扑排序，长度最小的树一定是 长度最长的树的一半（一定要审题，一开始我还以为是连接叶子节点的点），因此只能有一个点或者
        ##两个点。用到了python中的函数collection.defauledict()跟dict一样http://www.cnblogs.com/herbert/archive/2013/01/09/2852843.html
                    
        
    
                
            
            
            
             
        
