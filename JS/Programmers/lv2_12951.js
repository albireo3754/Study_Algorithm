function solution(s) {
  const a = s
    .split(' ')
    .map((x) => {
      if (x === '') return '';
      return x[0].toUpperCase() + x.slice(1).toLowerCase();
    })
    .join(' ');
  return a;
}
