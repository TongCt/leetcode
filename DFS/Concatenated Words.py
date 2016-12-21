class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        wordset = set(words)
        for w in words:
            
            
            wordset.remove(w)
            if(dfs(w,wordset)==True):
                result.append(w)
            wordset.add(w)
        return result
            
        
def dfs(strs,words):
    length = len(strs)
    if strs in words:
        return True
    for i in range(1,length):
        if(strs[:i] in words):
            if(dfs(strs[i:],words)):
                return True
            
    return False
            
            
            
            
