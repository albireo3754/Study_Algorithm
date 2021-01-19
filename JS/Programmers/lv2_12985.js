function solution(n, a, b) {
  let mid = n / 2;
  let add = n / 2;
  let cnt = 1;
  if (a > b) {
    [a, b] = [b, a];
  }
  while (a != b) {
    a = a % 2 === 1 ? (a + 1) / 2 : a / 2;
    b = b % 2 === 1 ? (b + 1) / 2 : b / 2;
    cnt++;
  }
  return --cnt;
}
