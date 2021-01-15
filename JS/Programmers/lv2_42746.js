function solution(numbers) {
  const numbersArray = numbers
    .map((a) => {
      return a.toString();
    })
    .sort((a, b) => b + a - (a + b))
    .join('');
  return numbersArray - 0 ? numbersArray : '0';
}
