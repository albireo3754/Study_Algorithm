function isCorrect(string) {
  const bracket = [];
  for (let i of string) {
    if (i === '(') bracket.push(1);
    else if (i === ')') {
      if (bracket.length === 0) {
        return false;
      }
      bracket.pop();
    }
  }
  return bracket.length === 0;
}

function isBalanced(string) {
  return (
    [...string].reduce((acc, cur) => {
      return cur === '(' ? acc + 1 : acc - 1;
    }, 0) === 0
  );
}

function solution(p) {
  if (isCorrect(p)) return p;
  let idx = 2;
  for (let i = 2; i < p.length + 1; i += 2) {
    if (isBalanced(p.slice(0, i))) {
      idx = i;
      break;
    }
  }
  const u = p.slice(0, idx);
  const v = p.slice(idx);
  if (isCorrect(u)) {
    return u + solution(v);
  }
  return `(${solution(v)})${[...u.slice(1, u.length - 1)]
    .map((x) => {
      return x === ')' ? '(' : ')';
    })
    .join('')}`;
}
