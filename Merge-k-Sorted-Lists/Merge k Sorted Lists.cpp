/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
private:
struct cmp{
    bool operator()(const ListNode* a,const ListNode* b){//不是特别了解模板是怎么回事
        return a->val>b->val;
    }
};
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int n = lists.size();
        if(n==0){
            return NULL;
        }
        priority_queue<ListNode*,vector<ListNode*>,cmp> que;
        ListNode dummy =NULL;
        ListNode* res =&dummy;
        
        for(int i=0;i<n;++i){
            if(lists[i]){
                que.push(lists[i]);//把所有的list的头节点都放到堆里
            }
        }
        
        while(!que.empty()){
            ListNode* p = que.top();//取出堆里最小的List的最小的数
            que.pop();
            res->next = p;
            res=p;
            if(p->next){
                que.push(res->next);//把list中次结点放到堆里
            }
            
        }
        return dummy.next;
        
    }
    
    
};
