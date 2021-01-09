// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(X, A) {
  // write your code in JavaScript (Node.js 8.9.4)
  var routes = new Array(X + 1);
  routes = routes.fill(0);

  for (var idx = 0; idx < A.length; idx++) {
    if (routes[A[idx]] === 0) {
      routes[A[idx]] = 1;
      X = X - 1;
    }
    if (X === 0) {
      return idx;
    }
  }
  return -1;
}
