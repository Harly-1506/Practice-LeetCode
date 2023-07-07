class Solution1 {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left = 0, right = 0, sumOfCurrent = 0;
        int res = INT_MAX;

        for(right = 0; right < nums.size(); right ++){
            sumOfCurrent += nums[right];

            while (sumOfCurrent >= target){
                res = min(res, right - left + 1);
                sumOfCurrent -= nums[left];
                left ++;
            }
        }
        return res == INT_MAX ? 0 : res;
    }
};

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
            
        int left = 0;
        int minLength = INT_MAX;
        int currentSum = 0;

        for (int right = 0; right < nums.size(); right++) {
            currentSum += nums[right];
            
            while (currentSum >= target) {
                minLength = std::min(minLength, right - left + 1);
                currentSum -= nums[left];
                left++;
            }
        }

        return (minLength == INT_MAX) ? 0 : minLength;
    }
};