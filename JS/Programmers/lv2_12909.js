function solution(s) {
  let answer = true;
  let stack = [];
  // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
  for (let i of s) {
    if (i === '(') stack.push(i);
    else {
      if (stack.length !== 0 && stack.pop() === '(') continue;
      return false;
    }
  }
  return stack.length === 0 ? true : false;
}
