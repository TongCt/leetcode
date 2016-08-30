/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* sortList(ListNode* head) {
       
        if(head == NULL || head->next == NULL) return head;
    
         ListNode* fast = head;
         ListNode* slow = head;
        while(fast->next && fast->next->next){
            fast = fast->next->next;
            slow = slow->next;
        }
        fast = slow;
        //ListNode* mid = slow->next;
        slow = slow->next;
        fast->next = NULL;
        
        ListNode* l1 = sortList(head);
        ListNode* l2 = sortList(slow);
        return mergesort(l1,l2);
    }
    
    ListNode* mergesort(ListNode* l1, ListNode* l2){
     /*   if(l1 == nullptr){
            return l2;
        }
        if(l2 == nullptr){
            return l1;
        }*/
        
        ListNode dummy(0);
        ListNode* cur = &dummy;
        while(l1 != NULL && l2 != NULL){
            if(l1->val < l2->val){
                cur->next = l1;
                l1 = l1->next;
            }
            else{
                cur->next = l2;
                l2 = l2->next;
            }
            
            cur = cur->next;
        }
        cur->next = l1? l1:l2;
        
        return dummy.next;
        
    }
};
    
    
