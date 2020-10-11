// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  A.sort();

  while (true) {
    var centerPos = (A.length + 1) / 2;
    if (cetnerPos === 1) {
      break;
    }
    if (A[centerPos] === A[cetnerPos - 1]) {
      A.slice(centerPos + 1);
    } else {
      A.slice(0, centerPos);
    }
  }
}

console.log(solution([42, 21, 13, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 42, 13]));
//return 7
