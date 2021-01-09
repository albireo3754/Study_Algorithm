function solution(strings, n) {
  let answer = [];
  answer = [...strings];
  answer.sort((x, y) => {
    if (x[n] < y[n]) {
      return -1;
    }
    if (x[n] > y[n]) {
      return 1;
    }
    if (x >= y) {
      return 1;
    }
    return -1;
  });
  return answer;
}
