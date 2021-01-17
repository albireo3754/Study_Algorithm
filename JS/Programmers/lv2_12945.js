function solution(n) {
  const fib = new Array(n + 1);
  fib[0] = 0;
  fib[1] = 1;
  for (let i = 2; i < n + 1; i++) {
    fib[i] = (fib[i - 1] + fib[i - 2]) % 1234567;
  }
  return fib[n];
}
