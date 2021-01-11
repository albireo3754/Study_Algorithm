function solution(land) {
  const answer = [...land];
  for (let i = 1; i < answer.length; i++) {
    for (let j = 0; j < 4; j++) {
      answer[i][j] += Math.max(
        ...answer[i - 1].slice(0, j),
        ...answer[i - 1].slice(j + 1)
      );
    }
  }
  return Math.max(...answer[answer.length - 1]);
}

// The function below is 0 score. Not make new answer array, but use arguments.
// function solution(land) {
//   const answer = [0, 0, 0, 0];
//   for (let i = 0; i < answer.length; i++) {
//     let score = land[0][i];
//     let col = i;
//     for (let j = 1; j < land.length; j++) {
//       const mapRow = land[j]
//         .map((cur, idx) => (idx === col ? [-1, idx] : [cur, idx]))
//         .sort((a, b) => b[0] - a[0]);
//       score += mapRow[0][0];
//       col = mapRow[0][1];
//     }
//     answer[i] += score;
//   }
//   return Math.max(...answer);
// }
