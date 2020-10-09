
function solution(N) {
  // write your code in JavaScript (Node.js 8.9.4)

  let maxBgap = 0;
  let binarys = [];

  var nearN = 1;
  let powerSize = 0;

  for (; N >= nearN; ) {
    powerSize += 1;
    nearN *= 2;
  }
  nearN /= 2;
  powerSize -= 1;

  for (; powerSize >= 0; powerSize--) {
    if (N >= nearN) {
      N -= nearN;
      binarys.push(1);
    } else {
      binarys.push(0);
    }
    nearN /= 2;
  }

  let bgap = 0;
  console.log(binarys);
  for (let n = 1; n < binarys.length; n++) {
    if (binarys[n] === 1) {
      if (maxBgap < bgap) {
        maxBgap = bgap;
        //bgap = 0; is wrong answer t.t
      }
      bgap = 0;
    } else {
      bgap += 1;
    }
  }
  //  0< maxgap <infinite
  return maxBgap;
}

console.log(solution(74901729));
