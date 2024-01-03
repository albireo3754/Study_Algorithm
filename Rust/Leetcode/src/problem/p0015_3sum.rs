use std::collections::HashSet;

/**
 * [15] 3Sum
 *
 * Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
 * Notice that the solution set must not contain duplicate triplets.
 *  
 * <strong class="example">Example 1:
 * 
 * Input: nums = [-1,0,1,2,-1,-4]
 * Output: [[-1,-1,2],[-1,0,1]]
 * Explanation: 
 * nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
 * nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
 * nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
 * The distinct triplets are [-1,0,1] and [-1,-1,2].
 * Notice that the order of the output and the order of the triplets does not matter.
 * 
 * <strong class="example">Example 2:
 * 
 * Input: nums = [0,1,1]
 * Output: []
 * Explanation: The only possible triplet does not sum up to 0.
 * 
 * <strong class="example">Example 3:
 * 
 * Input: nums = [0,0,0]
 * Output: [[0,0,0]]
 * Explanation: The only possible triplet sums up to 0.
 * 
 *  
 * Constraints:
 * 
 * 	3 <= nums.length <= 3000
 * 	-10^5 <= nums[i] <= 10^5
 * 
 */
pub struct Solution {}

// problem: https://leetcode.com/problems/3sum/
// discuss: https://leetcode.com/problems/3sum/discuss/?currentPage=1&orderBy=most_votes&query=

// submission codes start here

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums = nums;
        nums.sort();
        let mut result = Vec::new();

        for i in 0..=(nums.len() - 2) {
            let mut j = i + 1;
            let mut k = nums.len() - 1;
            if i > 0 && nums[i] == nums[i - 1] {
                continue;
            }
            while j < k {
                let mut sum_3 = nums[i] + nums[j] + nums[k];
                if sum_3 == 0 {
                    result.push(vec![nums[i], nums[j], nums[k]]);
                    j += 1;
                    k -= 1;
                    while j < nums.len() && nums[j] == nums[j - 1] {
                        j += 1;
                    }

                    while k > 0 && nums[k] == nums[k + 1] {
                        k -= 1;
                    }
                } else if sum_3 < 0 {
                    j += 1;
                } else {
                    k -= 1;
                }
            }
        }
        result
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_15_2() {
        assert_eq!(Solution::three_sum(vec![0,0,0]), vec![vec![0, 0, 0]]);
    }
    #[test]
    fn test_15() {
        assert_eq!(Solution::three_sum(vec![-1, 0, 1, 2, -1, 4]), vec![vec![-1, -1, 2], vec![-1, 0, 1]]);
        assert_eq!(Solution::three_sum(vec![-1, 0, 1, 2, -1, 4]), vec![vec![-1, -1, 2], vec![-1, 0, 1]]);
    }
}