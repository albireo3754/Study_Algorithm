function solution(m, n, board) {
  function checkBlock(x, y, friends) {
    return (
      friends === board[x + 1][y] &&
      friends === board[x][y + 1] &&
      friends === board[x + 1][y + 1]
    );
  }
  let answer = 0;
  let flag = true;
  let visited = board.map((x) => new Array(x.length));
  while (flag) {
    flag = false;
    for (let i = 0; i < m - 1; i++) {
      for (let j = 0; j < n - 1; j++) {
        if (board[i][j] === '0') continue;
        if (board[i][j] && checkBlock(i, j, board[i][j])) {
          visited[i][j] = 1;
          visited[i + 1][j] = 1;
          visited[i][j + 1] = 1;
          visited[i + 1][j + 1] = 1;
          flag = true;
        }
      }
    }

    for (let i = 0; i < m; i++) {
      for (let j = 0; j < n; j++) {
        if (visited[i][j] !== 1) continue;
        visited[i][j] = 0;
        answer++;
        for (let k = i; k > 0; k--) {
          board[k] =
            board[k].slice(0, j) + board[k - 1][j] + board[k].slice(j + 1);
          board[k - 1] =
            board[k - 1].slice(0, j) + '0' + board[k - 1].slice(j + 1);
        }
      }
    }
  }
  return answer;
}

// function rotateBoard(m, n, board) {
//   const nBoard = [];
//   for (let n = 0; n < board[0].length; n++) {
//     // col
//     let arr = [];
//     for (let m = 0; m < board.length; m++) {
//       arr.push(board[m][n]);
//     }
//     nBoard.push(arr.reverse().join(''));
//   }
//   return nBoard;
// }

// function solution(m, n, board) {
//   let answer = 0;
//   let nBoard = rotateBoard(m, n, board);
//   //row
//   //모든 보드판을 한번 쑥 훝는 케이스
//   function checkSquare(x, y, friends) {
//     if (
//       nBoard[x + 1][y] === friends &&
//       nBoard[x][y + 1] === friends &&
//       nBoard[x + 1][y + 1] === friends
//     ) {
//       return true;
//     } else return false;
//   }
//   function deleteSquare(arr) {
//     arr.forEach((coordi) => {
//       let reg = new RegExp(coordi[0], 'g');
//       nBoard[coordi[1]] =
//         nBoard[coordi[1]].slice(0, coordi[2]) +
//         nBoard[coordi[1]].slice(coordi[2], coordi[2] + 2).replace(reg, '0') +
//         nBoard[coordi[1]].slice(coordi[2] + 2);
//       nBoard[coordi[1] + 1] =
//         nBoard[coordi[1] + 1].slice(0, coordi[2]) +
//         '00' +
//         nBoard[coordi[1] + 1].slice(coordi[2] + 2);
//     });
//   }
//   while (true) {
//     let willDelete = [];
//     for (let x = 0; x < nBoard.length - 1; x++) {
//       for (let y = 0; y < nBoard[x].length - 1; y++) {
//         if (checkSquare(x, y, nBoard[x][y])) {
//           willDelete.forEach((coordi) => {
//             if (coordi[0] === nBoard[x][y]) {
//               if (Math.abs(coordi[1] - x) === 1 && Math.abs(coordi[2] - y)) {
//                 answer -= 1;
//               } else if (
//                 Math.abs(coordi[1] - x) === 1 ||
//                 Math.abs(coordi[2] - y)
//               ) {
//                 answer -= 2;
//               }
//             }
//           });
//           willDelete.push([nBoard[x][y], x, y]);
//           answer += 4;
//         }
//       }
//     }
//     deleteSquare(willDelete);
//     if (willDelete.length === 0) return answer;
//     nBoard = nBoard.map((str) => str.replace(/0/g, ''));
//     console.log(nBoard);
//   }
// }
