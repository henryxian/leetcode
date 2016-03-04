// 228. Summary Ranges My Submissions Question

// class Solution {
// public:
//     vector<string> summaryRanges(vector<int>& nums) {
//         vector<string> vec_str;
//         auto beg = nums.cbegin();
//         auto end = beg;
//         while (end != nums.cend()) {
//             while (end + 1 != nums.cend() && *(end + 1) - *end == 1)
//                 end++;
//             if (beg == end)
//                 vec_str.push_back(to_string(*beg));
//             else
//                 vec_str.push_back(to_string(*beg) + "->" + to_string(*end));
//             beg = end + 1;
//             end = beg;
//         }
//         return vec_str;
//     }
// };

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> vec_str;
        auto beg = 0;
        auto end = beg;
        auto size = nums.size();
        while (end < size) {
            while (end + 1 < size && nums[end + 1] - nums[end] == 1)
                end++;
            if (beg == end)
                vec_str.push_back(to_string(nums[beg]));
            else
                vec_str.push_back(to_string(nums[beg]) + "->" + to_string(nums[end]));
            beg = end + 1;
            end = beg;
        }
        return vec_str;
    }
};