/**
 * [6] Zigzag Conversion
 *
 * The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
 * 
 * P   A   H   N
 * A P L S I I G
 * Y   I   R
 * 
 * And then read line by line: "PAHNAPLSIIGYIR"
 * Write the code that will take a string and make this conversion given a number of rows:
 * 
 * string convert(string s, int numRows);
 * 
 *  
 * <strong class="example">Example 1:
 * 
 * Input: s = "PAYPALISHIRING", numRows = 3
 * Output: "PAHNAPLSIIGYIR"
 * 
 * <strong class="example">Example 2:
 * 
 * Input: s = "PAYPALISHIRING", numRows = 4
 * Output: "PINALSIGYAHRPI"
 * Explanation:
 * P     I    N
 * A   L S  I G
 * Y A   H R
 * P     I
 * 
 * <strong class="example">Example 3:
 * 
 * Input: s = "A", numRows = 1
 * Output: "A"
 * 
 *  
 * Constraints:
 * 
 * 	1 <= s.length <= 1000
 * 	s consists of English letters (lower-case and upper-case), ',' and '.'.
 * 	1 <= numRows <= 1000
 * 
 */
pub struct Solution {}

// problem: https://leetcode.com/problems/zigzag-conversion/
// discuss: https://leetcode.com/problems/zigzag-conversion/discuss/?currentPage=1&orderBy=most_votes&query=

// submission codes start here
impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        
        let s= s.as_bytes();      
        let inter_len = std::cmp::max(0, num_rows - 2) as usize;
        let mut result = String::new();
        let num_rows = num_rows as usize;
        
        
            for row in 0..num_rows {
                let mut i = row as usize;
                while i < s.len() {
                    println!("{}", i);
                    result.push(s[i] as char);
                    i += num_rows;
                    i += inter_len;
                    if (row >= 1 && row < num_rows - 1 && i - row * 2 < s.len()) {
                        result.push(s[i - row * 2] as char);
                    }
                }
            }
        return result;
        // PAY / num_rows - 3 P (len: num_rows - 2) / ALI / S / HIR / I / NG
        // P A H A P L S I I G Y I R
        // 2일땐
        // P Y A
        // 3일땐
        // P     I
        // A   L
        // Y A  
        // P
    }
}

// submission codes end

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_6() {
    }
}