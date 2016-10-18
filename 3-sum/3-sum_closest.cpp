#include<iostream>
#include<algorithm>
#include<string>
#include<vector>

using namespace std;

class Solution {
public:
	int threeSumClosest(vector<int>& nums, int target) {
		int result = 0;
		sort(nums.begin(), nums.end());
		int min_gap = 10000000;
		for (auto a = nums.begin(); a != prev(nums.end(), 2); ++a) {

			auto b = next(a);
			auto c = prev(nums.end());
			while (b<c) {
				int sum = *a + *b + *c;
				int gap = abs(target - sum);
				if (gap<min_gap) {
					result = sum;
					min_gap = gap;
				}
				if (sum>target) {
					--c;
				}
				else {
					++b;
				}
			}
		}

		return result;

	}
};

int main() {
	vector<int> nums = { -1,2,1,-4 };
	Solution sl;
	int k =sl.threeSumClosest(nums, 1);
	cout << k << endl;
	return 0;
}




要注意C++迭代器的一个问题；
错误观点：通过vector：：end（）能获取指向最后一个元素的指针。
实际上，通过上面的方法获取的是指向末尾元素再下一个位置的指针。
因此prev(end()) 指的才是最后一个元素的值，end()-1也行。
