/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        vector<int> level;
        queue<TreeNode *> stack,next;
        TreeNode* p = nullptr;
       // int level = 0;
        if (root == NULL){
            return result;
        }
        stack.push(root);
        while(!stack.empty()){
           
            while(!stack.empty())
            {
                p=stack.front();
                stack.pop();
                level.push_back(p->val);
                if(p->left != NULL){
                    next.push(p->left);
                }
                if(p->right != NULL){
                    next.push(p->right);
                }
            }
            result.push_back(level);
            level.clear();
            swap(next,stack);
        }
        return result;
        
    }
};
其实本质是层次遍历，这是非递归的做法，借助两个队列一个数组
