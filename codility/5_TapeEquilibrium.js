// Task Score
// 100%
// Correctness
// 100%
// Performance
// 100%

function solution(A) {
  var minDiff;
  if (A.length == 2) {
    return Math.abs(A[0] - A[1]);
  }
  var sumFromLast = A.reduce((acc, cuv) => acc + cuv, 0) - A[0];
  var sumFromFirst = A[0];
  minDiff = Math.abs(sumFromLast - sumFromFirst);

  for (var idx = 1; idx < A.length - 1; idx++) {
    sumFromFirst += A[idx];
    sumFromLast -= A[idx];

    var diff = Math.abs(sumFromLast - sumFromFirst);

    if (diff < minDiff) {
      minDiff = diff;
    }
  }
  return minDiff;
}
console.log(solution([3, 1, 2, 4, 3]));
