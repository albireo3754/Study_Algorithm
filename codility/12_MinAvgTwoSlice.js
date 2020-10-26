// 1. score 0% -> this algorithm is so trash
// 2. score 64% -> solution of 1st, but can not improve at this station.

function solution(A) {
  var minValue = (A[0] + A[1]) / 2;
  var minIdx = 0;
  for (var idx = 2; idx < A.length; idx++) {
    var minThree = (A[idx - 2] + A[idx - 1] + A[idx]) / 3;
    var minTwo = (A[idx - 1] + A[idx]) / 2;

    if (minValue > minTwo) {
      minValue = minTwo;
      minIdx = idx - 1;
    }
    if (minValue > minThree) {
      minValue = minThree;
      minIdx = idx - 2;
    }
  }
  return minIdx;
}
