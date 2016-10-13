class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int heap_size = nums.size();
         
        sort_heap(nums,heap_size);
        
        return nums[heap_size-k];
        
        
    }
    
    void max_heap(vector<int>& nums,int parent,int heap_size){
        int l = parent*2+1;
        int r = parent*2+2;
        int largest = parent;
        if(l<heap_size && nums[l]>nums[parent]){
            largest = l;
        }
        if(r<heap_size && nums[r]>nums[largest]){
            largest = r;
        }
        if(largest != parent){
            swap(nums[parent],nums[largest]);
            max_heap(nums,largest,heap_size);
        }
        
    }
    
    void build_heap(vector<int>& nums,int heap_size){
        for(int i=(heap_size/2 -1);i>=0;i--){
            max_heap(nums,i,heap_size);
        }
    }
    
    void sort_heap(vector<int>& nums,int heap_size){
        build_heap(nums,heap_size);
        for(int i = heap_size -1;i>0;i--){
            swap(nums[0],nums[i]);
            heap_size--;
            max_heap(nums,0,heap_size);
            
        }
    }
};

用heap排序，然后找出来第Kth大的，算法比较慢，

改进版理论上复杂度一样，但是实际上会快一点：

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int heap_size = nums.size();
         
        int kth = sort_heap(nums,heap_size,k);
        
        return kth ;
        
        
    }
    
    void max_heap(vector<int>& nums,int parent,int heap_size){
        int l = parent*2+1;
        int r = parent*2+2;
        int largest = parent;
        if(l<heap_size && nums[l]>nums[parent]){
            largest = l;
        }
        if(r<heap_size && nums[r]>nums[largest]){
            largest = r;
        }
        if(largest != parent){
            swap(nums[parent],nums[largest]);
            max_heap(nums,largest,heap_size);
        }
        
    }
    
    void build_heap(vector<int>& nums,int heap_size){
        for(int i=(heap_size/2 -1);i>=0;i--){
            max_heap(nums,i,heap_size);
        }
    }
    
    int  sort_heap(vector<int>& nums,int heap_size,int k){
        build_heap(nums,heap_size);
        int kth =0;
        int cun =0;
        for(int i = heap_size -1;cun!=k;i--){
            kth = nums[0];
            cun++;
            swap(nums[0],nums[i]);
            heap_size--;
            max_heap(nums,0,heap_size);
        }
        return kth;
    }
};
