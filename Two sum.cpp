class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        map<int,int>mapping;
        
        
        for(int i =0;i<nums.size();i++){
            if(mapping.find(target-nums[i]) != mapping.end()){
                result.push_back(mapping[target-nums[i]]);
                result.push_back(i);
                break;
            }
            mapping[nums[i]] = i;
        }
    return result;
    
    }
        
        
   };
这一题要返回位置坐标，因此不能用双指针，先排序nlog(n),然后用双指针从两边进行查找，

主要用hash，O(n)，比较简单，掌握map的用法
