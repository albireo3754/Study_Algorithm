function solution(s) {
  return s
    .split(' ')
    .map((x) => Number(x))
    .sort((a, b) => a - b)
    .filter((_, i) => i === 0 || i === s.split(' ').length - 1)
    .join(' ');
}
