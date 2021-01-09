function solution(a, b) {
  let answer = 0;

  if (b > a) {
    for (let i = a; i < b + 1; i += 1) answer += i;
  } else {
    for (let i = b; i < a + 1; i += 1) answer += i;
  }
  return answer;
}
