function solution(s) {
  if (s.length !== 4 && s.length !== 6) return false;

  for (let v of s) {
    if (Number.isNaN(v)) return false;
  }
  return true;
}
