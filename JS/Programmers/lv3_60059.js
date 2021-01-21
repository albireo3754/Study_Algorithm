function rotation(key) {
  const M = key.length;
  const result = new Array(M).fill(0).map(_ => []);
  for (let i = 0; i < M; i++) {
    for (let j = 0; j < M; j++) {
      result[j][M - 1 - i] = key[i][j];
    }
  }
  return result;
}
function match(board, M) {
  const N = board.length;
  for (let i = M; i < N - M; i++) {
    for (let j = M; j < N - M; j++) {
      if (board[i][j] === 0) return false;
    }
  }
  return true;
}
function isLock(key, board) {
  const M = key.length;
  const N = board.length;
  for (let x = 0; x < N - M; x++) {
    for (let y = 0; y < N - M; y++) {
      let mBoard = makeBoard(board);
      for (let i = 0; i < M; i++) {
        for (let j = 0; j < M; j++) {
          if (key[i][j] === 0) continue;
          // key is 1
          mBoard[i + x][j + y] ^= 1;
          // if (mBoard[i + x][j + y] === 1;
        }
      }
      // console.log(match(mBoard, M));
      if (match(mBoard, M)) return true;
    }
  }
  return false;
}
function makeBoard(template) {
  return template.map(x => [...x]);
}
function solution(key, lock) {
  let M = key.length;
  let N = lock.length;
  let template = [];
  for (let i = 0; i < M * 2 + N; i++) {
    template.push(Array(M * 2 + N));
    if (i < M || i >= M + N) {
      template[i].fill(0);
      continue;
    }
    for (let j = 0; j < M * 2 + N; j++) {
      if (j < M || j >= key.length + N) {
        template[i][j] = 0;
      } else {
        template[i][j] = lock[i - M][j - M];
      }
    }
  }

  for (let i = 0; i < 4; i++) {
    if (isLock(key, template)) return true;
    key = rotation(key);
  }
  return false;
}
