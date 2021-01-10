function solution(s) {
  const strArray = [...s].sort().reverse();
  return strArray.join().replace(/,/g, '');
}
