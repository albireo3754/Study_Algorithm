function solution(numbers) {
  const numbersArray = numbers
    .map((a) => {
      return a.toString();
    })
    .sort((a, b) => b + a - (a + b))
    .join('');
  return numbersArray - 0 ? numbersArray : '0';
}

// `${b}${a}` - `${a}${b}` is (to string) plus (b + a - (a + b)) function
