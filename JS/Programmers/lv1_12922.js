function solution(n) {
  const pattern = '수박';
  const answer = [];
  if (n % 2 === 0) {
    for (let i = 0; i < n / 2; i++) {
      answer.push(pattern);
    }
  } else {
    for (let j = 0; j < n / 2 - 1; j++) {
      answer.push(pattern);
    }
    answer.push('수');
  }
  return answer.join('');
}

// if i use string.prototype.repeat() => can show like string * 5 ,python3;
