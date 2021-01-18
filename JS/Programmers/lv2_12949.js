function solution(arr1, arr2) {
  let m = arr1.length;
  let n = arr2[0].length;
  const answer = [];
  for (let i = 0; i < m; i++) {
    answer.push([]);
    for (let j = 0; j < n; j++) {
      let result = 0;
      for (let x = 0; x < arr1[0].length; x++) {
        result += arr1[i][x] * arr2[x][j];
      }
      answer[i].push(result);
    }
  }
  return answer;
}
