function solution(n) {
  let answer = new Array(n + 1);
  for (let i = 0; i < n + 1; i += 1) {
    answer[i] = new Array(i);
  }
  let direction = 1;
  let [x, y] = [0, 0];
  let side = n + 1;
  let cnt = 0;
  for (let j = 1; j < (n * (n + 1)) / 2 + 1; j += 1) {
    if (cnt === 0) {
      side -= 1;
      cnt = side;
      direction = direction === 1 ? -1 : direction + 1;
    }
    if (direction === -1) {
      x += 1;
    } else if (direction === 0) {
      y += 1;
    } else if (direction === 1) {
      x -= 1;
      y -= 1;
    }
    answer[x][y] = j;
    cnt -= 1;
  }
  return answer.reduce((acc, cur) => [...acc, ...cur]);
}
