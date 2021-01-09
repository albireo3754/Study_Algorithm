//1. score is 0% why? => if A is [3], solution return 4 ,but expected 1
// => solution => add return 1 if start value is not over 1
//2. score is 22% why? => adding start positive fixed only first problem
// there must be very big code problem.
// => solution => js array sort function need argument of comparefunction
// if there is no comparefunction, it sort 1,100,2,3 like string not int

function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  A.sort(function (a, b) {
    return a - b;
  });

  var smallestInt = 0;
  var startPositive = A.length - 1;
  for (var idx = 0; idx < A.length; idx++) {
    if (A[idx] > 0) {
      startPositive = idx;
      if (A[idx] > 1) {
        return 1;
      } else {
        break;
      }
    }
  }

  for (var idx = startPositive; idx < A.length; idx++) {
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
console.log(solution([1, 2, 3, 5, 6, 7]));
