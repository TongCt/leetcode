class Solution {
private:
        vector<vector<string>> res;
        
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<int> state(n,-1);
        helper(state,0);
        return res;
    }
    void helper(vector<int> &state, int raw){
        int n = state.size();
        if(raw == n){
            vector<string>temp(n,string(n,'.'));
            for(int i=0;i<n;i++){
                temp[i][state[i]] = 'Q';
            }
            res.push_back(temp);
            return;
        }
        
        for(int col=0;col<n;col++){
            if(isvalid(raw,col,state)){
                state[raw] = col;
                helper(state,raw+1);
                state[raw] = -1;//????
            }
         
        }
        
    }
    
    
    bool isvalid(int raw,int col,vector<int> &state){
        for(int i=0;i<raw;i++){
            if(abs(i-raw) == abs(state[i]-col) || state[i] == col){
                return false;
            }
        }
        return true;
    }
    
};
