class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i=0;
        res =0;
        
        size = len(A);
        dp=[0]*size;
        if size<3:
            return 0;
        for i in range(2,size):
            if(A[i]-A[i-1])==(A[i-1]-A[i-2]):
                dp[i]=dp[i-1]+1;
                res=res+dp[i];
            
        return res;
        
        
        python的解法：动态规划解dp[i]是第i个元素时arithmetic slice的数目
        
        python list的用法，
        声明一个全为全0数组
        dp=[0]*n;
        
        声明一个二维数组时，
        multilist = [[0 for col in range(5)] for row in range(3)]
        或者multilist = [[0] * 5 for row in range(3)]
        不能写成
        multi = [[0] * 5] * 3 这只是把对象引用了三次
