//1. score is 0% why? => if A is [3], solution return 4 ,but expected 1
// => solution =>

function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  var intsDict = {};
  var max = 0;
  for (var idx = 0; idx < A.length; idx++) {
    var compareInt = A[idx];
    intsDict[compareInt] = compareInt;
    if (compareInt > max) {
      max = compareInt;
    }
  }

  for (var int = 1; int < A.length + 1; int++) {
    if (intsDict[int] === undefined) {
      return int;
    }
  }
  return max + 1;
}
console.log(solution([2]));
