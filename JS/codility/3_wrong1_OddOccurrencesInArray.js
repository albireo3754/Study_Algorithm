// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  for (; A.length > 1; ) {
    var find = A[0];
    A = A.slice(1);
    var locIdx = A.indexOf(find);
    console.log(1);
    if (locIdx === -1) {
      A = A.concat(find); // !!concat function returns new array
      //그냥 여기서
      //return find
      //하면안되나?
    } else {
      A.splice(locIdx, 1);
    }
  }

  return A[0];
}

console.log(solution([42, 21, 13, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 42, 13]));
//return 7
