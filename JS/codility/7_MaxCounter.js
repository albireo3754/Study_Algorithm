// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');
function maxab(a, b) {
  if (a > b) {
    return a;
  } else {
    return b;
  }
}

function solution(N, A) {
  // write your code in JavaScript (Node.js 8.9.4)
  var counters = new Array(N);
  counters = counters.fill(0);
  var max = 0;
  var tmpmax = 0;

  for (var idx = 0; idx < A.length; idx++) {
    if (A[idx] == N + 1) {
      max = tmpmax;
    } else {
      if (counters[A[idx] - 1] < max) {
        counters[A[idx] - 1] = max + 1;
      } else {
        var tmpmax = maxab(tmpmax, counters[A[idx] - 1] + 1);
        counters[A[idx] - 1] = tmpmax;
      }
    }
    console.log(counters);
  }

  for (var idx = 0; idx < A.length; idx++) {
    if (counters[idx] < max) {
      counters[idx] = max;
    }
  }
  console.log(counters);
  return counters;
}

console.log(solution(5, [3, 4, 4, 6, 1, 4, 4]));
