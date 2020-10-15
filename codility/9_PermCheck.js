//1. 41% why? => I think to be able to permit number repeat.
//But this translation is wrong.
//solution => will the sort algorithm work in time?

function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)

  var numDict = {};

  for (var idx = 0; idx < A.length; idx++) {
    numDict[A[idx]] = A[idx];
  }

  for (var key = 1; key <= Object.keys(numDict).length; key++) {
    if (numDict[key] === undefined) {
      return 0;
    }
  }
  return 1;
}
