// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  A.sort();

  var smallestInt = 0;
  for (var idx = 0; idx < A.length; idx++) {
    if (idx == A.length - 1) {
      smallestInt = A[idx] + 1;
    } else if (A[idx] + 2 <= A[idx + 1]) {
      return A[idx] + 1;
    }
  }

  if (smallestInt <= 1) {
    return 1;
  }
  return smallestInt;
}

console.log(solution([3]));
