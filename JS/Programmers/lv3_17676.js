function solution(lines) {
  let answer = 0;
  const newLines = [];
  // 2016-09-15 01:00:04.001 2.0s
  for (let line of lines) {
    let lineSplit = line.split(" ");
    let [h, m, s] = lineSplit[1].split(":").map(time => Number(time));
    s += m * 60 + h * 3600;
    s *= 1000;
    let during = Number(lineSplit[2].slice(0, lineSplit[2].length - 1));
    newLines.push([Math.round(s - during * 1000 + 1), Math.round(s)]);
  }
  // console.log(newLines);
  // console.log('loop')
  for (let i = newLines.length - 1; i > -1; i--) {
    let start = newLines[i][1];
    let end = newLines[i][1] + 1000 - 1;
    let cnt = 1;
    for (let j = i - 1; j > -1; j--) {
      if (start <= newLines[j][1]) cnt++;
      else break;
    }
    for (let k = i + 1; k < newLines.length; k++) {
      // console.log(newLines[k][0], end)
      if (newLines[k][0] <= end) cnt++;
    }
    if (cnt > answer) answer = cnt;
  }
  return answer;
}
