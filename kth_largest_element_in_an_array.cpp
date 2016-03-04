// 215. Kth Largest Element in an Array

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
         if (nums.size() == 0) {
             return -1;
         }
         k = nums.size() - k + 1;
         int start = 0;
         int end = nums.size() - 1;
         int index = partition(nums, start, end);
         while (index != k - 1) {
             if (index < k - 1) {
                start = index + 1;
                index = partition(nums, start, end);
             } else {
                end = index - 1;
                index = partition(nums, start, end);
             }
         }
         return nums[index];
    }
    
    int partition(vector<int>& nums, int l, int r) {
        int pivot = nums[l]; // notice here
        int tmp;
        while (l < r) {
            while (nums[r] >= pivot && l < r) {
                r--;
            }
            if (l < r) {
                tmp = nums[l];
                nums[l] = nums[r];
                nums[r] = tmp;
                l++;
            }
            
            while (nums[l] <= pivot && l < r) {
                l++;
            }
            if (l < r) {
                tmp = nums[l];
                nums[l] = nums[r];
                nums[r] = tmp;
                r--;
            }
        }
        nums[l] = pivot;
        // cout << l << endl;
        return l;
    }
};