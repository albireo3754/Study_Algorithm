// CyclicRotation
// JavaScript
// 34 min
// 87%

// Wrong
// small2
// small functional tests, K >= N   ✘WRONG ANSWER
// got [1, 1, 2, 3, 5] expected [3, 5, 1, 1, 2]

// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A, K) {
  // write your code in JavaScript (Node.js 8.9.4)

  let Asize = A.length;
  let cycleIndex;
  let cycleA;

  // 2nd problem, if i add this it reached limit time out

  // if (Asize >= K) {
  //   cycleIndex = Asize - K;
  // } else {
  //   for (; K > Asize; ) {
  //     K = K - Asize; // add this, if Asize == 10, K is the bigger~~ it makes trouble
  //   }
  //   cycleIndex = Asize - K;
  // }

  if (Asize < K) {
    K = K % Asize;
  }
  cycleIndex = Asize - K;

  for (cycleIndex; cycleIndex > Asize; ) {
    cycleIndex = cycleIndex - K;
  }

  let frontA = A.slice(cycleIndex);
  let frontB = A.slice(0, cycleIndex);

  cycleA = frontA.concat(frontB);

  return cycleA;
}

solution([3, 8, 9, 7, 6], 13);
