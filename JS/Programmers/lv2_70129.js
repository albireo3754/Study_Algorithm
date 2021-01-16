function solution(s) {
  let s_ = s.slice(0);
  const answer = [0, 0];
  while (s_.length !== 1) {
    answer[0] += 1;
    let c = s_.replace(/0/g, '').length;
    answer[1] += s_.length - c;
    s_ = c.toString(2);
  }
  return answer;
}
