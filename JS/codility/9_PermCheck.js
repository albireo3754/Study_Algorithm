//1. 41% why? => I think to be able to permit number repeat.
//But this translation is wrong.
//solution => will the sort algorithm work in time?

//2. 75% why? => sort of js is not stable sort. fucking this problem
// is in the previous problem.
function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)

  A.sort((a, b) => a - b);

  for (var idx = 0; idx < A.length; idx++) {
    if (A[idx] !== idx + 1) {
      return 0;
    }
  }
  return 1;
}
