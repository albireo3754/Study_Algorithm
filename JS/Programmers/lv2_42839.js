function makePrimeArray(size) {
  const primes = Array(size + 1).fill(-1);
  for (let i = 2; i ** 2 <= size; i++) {
    if (primes[i] === -1) primes[i] = i;
    let nonePrime = i + i;
    while (nonePrime < primes.length) {
      primes[nonePrime] = 0;
      nonePrime += i;
    }
  }
  primes[0] = 0;
  primes[1] = 0;
  return primes;
}

function permute(array) {
  if (array.length === 1) return array;
  const permutes = new Set();
  for (let i = 0; i < array.length; i++) {
    let subArray = [...array.slice(0, i), ...array.slice(i + 1)];
    for (let j of permute(subArray)) {
      if (j === '0') continue;
      permutes.add(j + array[i]);
      permutes.add(j);
    }
  }
  return permutes;
}
function solution(numbers) {
  const numArray = numbers.split('').sort((a, b) => b - a);
  const primes = makePrimeArray(Number(numArray.join('')));
  let answer = 0;
  const permutes = permute(numArray);
  for (let isPrime of permutes) {
    if (primes[isPrime]) answer++;
  }
  return answer;
}
