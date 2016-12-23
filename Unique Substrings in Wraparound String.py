class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        count =0;
        sum=0;
        res=[0 for i in range(26)];
        for i in range(len(p)):
            if(i>0 and ord(p[i])-ord(p[i-1])==1 or ord(p[i])-ord(p[i-1])==-25):
                count+=1;
            else:
                count=1;
            res[ord(p[i])-ord('a')]=max(count,res[ord(p[i])-ord('a')]);
            
            
        for i in range(26):
            sum=sum+res[i];
            
        return sum
        
        
        
