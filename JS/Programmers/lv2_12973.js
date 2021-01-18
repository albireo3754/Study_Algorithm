function solution(s) {
  let str = s.slice(0);
  const stack = [];
  [...s].forEach((x) => {
    if (stack.length === 0 || stack[stack.length - 1] !== x) stack.push(x);
    else if (stack[stack.length - 1] === x) {
      stack.pop();
      // while (stack.length > 1) {
      //     if (stack[stack.length - 1] === stack[stack.length - 2]) {
      //         stack.pop();
      //         stack.pop();
      //     } else break;
      // }
    }
  });
  return stack.length === 0 ? 1 : 0;
}
