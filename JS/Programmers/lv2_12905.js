function solution(board) {
  //  0 is row x and 1 is col y
  const x = board.length;
  const y = board[0].length;
  let max = 0;
  if (x <= 1 || y <= 1) return 1;

  for (let i = 1; i < x; i++) {
    for (let j = 1; j < y; j++) {
      if (board[i][j] >= 1) {
        const top = board[i - 1][j];
        const left = board[i][j - 1];
        const leftTop = board[i - 1][j - 1];
        const min = Math.min(top, left, leftTop);
        board[i][j] = min + 1;
        max = Math.max(max, min + 1);
      }
    }
  }
  return max ** 2;
}

// function solution(board) {
//   //  0 is row x and 1 is col y
//   let sizes = [[], []];
//   for (let x = 0; x < board.length; x++) {
//     sizes[0].push(board[x].reduce((acc, cur) => acc + cur));
//   }

//   for (let y = 0; y < board[0].length; y++) {
//     let count = 0;
//     for (let x = 0; x < board.length; x++) {
//       count += board[x][y];
//     }
//     sizes[1].push(count);
//   }
//   let lenMax = Math.min(sizes[0].length, sizes[1].length);
//   let canMake = [0, 0];
//   while (lenMax > 0) {
//     let xCnt = lenMax;
//     let yCnt = lenMax;
//     if (canMake[0] === 0) {
//       for (let x = 0; x < sizes[0].length; x++) {
//         if (lenMax <= sizes[0][x]) {
//           xCnt -= 1;
//         } else xCnt = lenMax;
//         if (xCnt === 0) {
//           canMake[0] = lenMax;
//           break;
//         }
//       }
//     }
//     if (canMake[1] === 0) {
//       for (let y = 0; y < sizes[1].length; y++) {
//         if (lenMax <= sizes[1][y]) {
//           yCnt -= 1;
//         } else yCnt = lenMax;
//         if (yCnt === 0) {
//           canMake[1] = lenMax;
//           break;
//         }
//       }
//     }
//     if (canMake[0] && canMake[1]) {
//       return Math.min(canMake[0], canMake[1]) ** 2;
//     }
//     lenMax -= 1;
//   }
//   return 0;
// }
