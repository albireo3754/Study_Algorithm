function solution(s, n) {
  let answer = '';
  for (let i of s) {
    if (i === ' ') {
      answer += i;
      continue;
    }
    let ascii = i.charCodeAt(0);
    if (ascii < 91) {
      if (ascii + n > 90) {
        ascii += n - 90 - 1 + 65;
      } else ascii += n;
    }
    if (ascii > 91) {
      if (ascii + n > 122) {
        ascii += n - 122 - 1 + 97;
      } else ascii += n;
    }
    answer += String.fromCharCode(ascii);
  }
  return answer;
}
