# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergetwoLists(l1,l2):
            dummy = ListNode(0);
            cur = dummy;
            while l1 and l2:
                if l1.val<l2.val:
                    cur.next = l1;
                    l1 = l1.next;
                else:
                    cur.next = l2;
                    l2 = l2.next;
                cur = cur.next;
            if(l1 or l2):
                cur.next = l1 or l2;
            return dummy.next
        
        def mergehelper(lists,begin,end):
            if begin > end:
                return None
            if begin==end:
                return lists[begin];
            return mergetwoLists(mergehelper(lists,begin,(begin+end)/2),mergehelper(lists,(begin+end)/2+1,end))
            
        return mergehelper(lists,0,len(lists)-1)
        
                    
            
        
        
        
