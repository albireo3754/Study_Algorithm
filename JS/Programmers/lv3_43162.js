function solution(n, computers) {
  let answer = 0;
  let visited = [];

  const dfs = function (node) {
    if (visited[node]) return 0;
    visited[node] = true;
    computers[node].forEach((cur, idx) => {
      if (cur === 1 && idx !== node) dfs(idx, visited);
    });
    return true;
  };

  for (let i = 0; i < n; i++) {
    if (dfs(i)) {
      answer++;
    }
  }

  // while (visited.length === n) {
  //     answer++;
  //     for (let i = 0; i < n; i++) {
  //         if (!visited[i]) {
  //             dfs[i];
  //             break;
  //         }
  //     }
  // }
  return answer;
}
