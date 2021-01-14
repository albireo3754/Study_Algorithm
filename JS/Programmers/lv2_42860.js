function solution(name) {
  let nameLen = name.length;
  let answer = 0;
  let moveMin = nameLen - 1;
  for (let i = 0; i < nameLen; i++) {
    let ascii = name[i].charCodeAt(0);
    answer += ascii <= 78 ? ascii - 65 : 91 - ascii;
    let nextIdx = i + 1;
    while (name[nextIdx] === 'A') nextIdx++;
    moveMin = Math.min(
      moveMin,
      i + nameLen - nextIdx + Math.min(i, nameLen - nextIdx)
    );
  }
  answer += moveMin;
  return answer;
}
