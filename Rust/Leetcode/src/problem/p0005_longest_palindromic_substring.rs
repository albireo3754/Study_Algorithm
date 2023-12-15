/**
 * [5] Longest Palindromic Substring
 *
 * Given a string s, return the longest <span data-keyword="palindromic-string">palindromic</span> <span data-keyword="substring-nonempty">substring</span> in s.
 *  
 * <strong class="example">Example 1:
 * 
 * Input: s = "babad"
 * Output: "bab"
 * Explanation: "aba" is also a valid answer.
 * 
 * <strong class="example">Example 2:
 * 
 * Input: s = "cbbd"
 * Output: "bb"
 * 
 *  
 * Constraints:
 * 
 * 	1 <= s.length <= 1000
 * 	s consist of only digits and English letters.
 * 
 */
pub struct Solution {}

// problem: https://leetcode.com/problems/longest-palindromic-substring/
// discuss: https://leetcode.com/problems/longest-palindromic-substring/discuss/?currentPage=1&orderBy=most_votes&query=

// submission codes start here

impl Solution {
    pub fn check_palindrome(s: &[u8], i: usize, j: usize, dp: &mut [[i32; 100]; 100]) -> bool {
        let mut _i = i;
        let mut _j = j;
        while _i <= _j {
            if dp[_i][_j] == 0 {
                if s[_i] != s[_j] {
                    dp[_i][_j] = -1;
                    return false;
                }
                _i += 1;
                _j -= 1;
            } else {
                if dp[_i][_j] == -1 {
                    return false;
                } else {
                    return true;
                }
            }
        }
        dp[i][j] = 1;
        return true;
    }
    pub fn longest_palindrome(s: String) -> String {
        let mut dp = [[0; 100]; 100];
        let bytes = s.as_bytes().to_owned();
        let mut s = String::from_utf8([bytes[0]].to_vec()).unwrap();
        for i in 0..=(bytes.len() / 2) {
            for j in ((bytes.len() / 2)..bytes.len()).rev() {
                if Solution::check_palindrome(&bytes, i, j, &mut dp) && s.len() < (j - i + 1) {
                    s = String::from_utf8(bytes[i..=j].to_vec()).unwrap();
                }
            }
        }
        return s;
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_5() {
        assert_eq!(Solution::longest_palindrome("bb".to_owned()), "bb".to_owned());
    }
}