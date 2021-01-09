// 1. 50% => timeout error O(B-A)
// 2. 100% => time complexity is O(1)
function solution(A, B, K) {
  // write your code in JavaScript (Node.js 8.9.4)

  return Math.floor(B / K) - Math.floor((A - 1) / K);
}
