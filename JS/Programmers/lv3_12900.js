function solution(n) {
  let a = 1;
  let b = 1;
  let c = 2;
  for (let i = 3; i < n + 1; i++) {
    [a, b, c] = [b, c, (b + c) % 1000000007];
  }
  return c;
}
