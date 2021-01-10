function solution(s) {
  let answer = 0;
  const sLower = s.toLowerCase();
  for (const a of sLower) {
    if (a === 'p') answer += 1;
    else if (a === 'y') answer -= 1;
  }
  return answer === 0;
}
