function solution(citations) {
  let answer = 0;
  const sortedCitations = [...citations].sort((b, a) => a - b);
  for (let i = 0; i < sortedCitations.length; i++) {
    if (sortedCitations[i] >= i + 1) {
      answer += 1;
    } else break;
  }
  return answer;
}
