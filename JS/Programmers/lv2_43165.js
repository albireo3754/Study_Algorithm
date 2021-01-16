function solution(numbers, target) {
  let answer = 0;
  function dfs(sum, idx) {
    if (idx === numbers.length) {
      if (sum === target) answer++;
    } else {
      dfs(sum + numbers[idx], idx + 1);
      dfs(sum + numbers[idx] * -1, idx + 1);
    }
  }
  dfs(0, 0);
  return answer;
}

// dfs(sum + numbers[idx] * -1, idx + 1); =>
// dfs(sum - numbers[idx], idx + 1); will be good!
