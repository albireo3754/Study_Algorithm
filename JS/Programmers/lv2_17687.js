function solution(n, t, m, p) {
  let answer = '';
  const game = [];
  let cnt = 1;
  for (let i = 0; i < t * m; i++) {
    for (let j of i.toString(n)) {
      game.push(j.toUpperCase());
      if (cnt++ % m === p % m) {
        answer += game.pop();
        if (answer.length === t) return answer;
      }
    }
  }
}
