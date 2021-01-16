function countOne(n) {
  return n.match(/1/g) ? n.match(/1/g).length : 0;
}
function solution(n) {
  let answer = n + 1;
  let oneOfN = countOne(n.toString(2));
  while (answer <= 1000000) {
    if (oneOfN === countOne(answer.toString(2))) return answer;
    answer += 1;
  }
  return answer;
}
