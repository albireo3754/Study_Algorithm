// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  A.sort();

  if (A.length === 0) {
    return A[0];
  }
  for (var i = 0; i < A.length; i = i + 2) {
    if (i + 1 === A.length) {
      return A[i];
    }
    if (A[i] !== A[i + 1]) {
      return A[i];
    }
  }
}
console.log(solution([2, 2, 3, 3, 4]));
//return 7
