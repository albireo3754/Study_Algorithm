// 100%

function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  var east = -1;
  var count = 0;
  var pairsOfPassingCars = 0;
  A = A.concat(0);
  console.log(A);
  for (var idx = 0; idx < A.length; idx++) {
    if (A[idx] === 0) {
      pairsOfPassingCars += (idx - east - 1) * count;
      count += 1;
      east = idx;
    }
  }
  if (pairsOfPassingCars > 1000000000) {
    return -1;
  }

  return pairsOfPassingCars;
}
