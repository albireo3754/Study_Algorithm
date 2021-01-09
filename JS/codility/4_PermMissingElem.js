// 1. PermMissingElem
// Find the missing element in a given permutation.
// Task Score
// 100%
// Correctness
// 100%
// Performance

function reducer(acc, cur, idx, a) {
  return acc + cur - idx;
}

function solution(A) {
  A.unshift(0);
  return A.length - A.reduce(reducer, 0);
}
console.log(solution([1, 2, 4, 5, 3, 7, 8, 10, 9]));
