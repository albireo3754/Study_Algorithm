const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().split('');

const inputs = input.split('\n');
// console.log(inputs);
const N = inputs[0].length;
const grid = Array(N + 1)
  .fill(0)
  .map(() =>
    Array(N + 1)
      .fill(0)
      .map(() => 0)
  );
// console.log(grid);

for (let i = 1; i <= N; i++) {
  for (let j = 1; j <= N; j++) {
    if (inputs[0][i - 1] === inputs[1][j - 1]) {
      grid[i][j] = grid[i - 1][j - 1] + 1;
    } else {
      grid[i][j] = Math.max(grid[i - 1][j], grid[i][j - 1]);
    }
  }
}
// console.log(grid);
let answer = grid[N][N];
if (!answer) {
  console.log(answer);
} else {
  console.log(answer);
  const lcs = [];
  let i = N;
  let j = N;
  while (answer > 0) {
    if (grid[i - 1][j] === grid[i][j]) {
      i--;
    } else if (grid[i][j] === grid[i][j - 1]) {
      j--;
    } else {
      // console.log(i, j);
      lcs.unshift(inputs[0][i - 1]);
      i--;
      j--;
      answer--;
    }
  }
  console.log(lcs.join(''));
}
