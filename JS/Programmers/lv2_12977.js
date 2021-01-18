function isPrime(n) {
  let a = 2;
  while (a ** 2 <= n) {
    if (n % a++ === 0) return false;
  }
  return true;
}

function solution(nums) {
  let odd = [],
    even = [];
  let answer = 0;
  nums.forEach((x) => {
    if (x % 2 === 0) even.push(x);
    else odd.push(x);
  });

  for (let i = 0; i < odd.length - 2; i++) {
    for (let j = i + 1; j < odd.length - 1; j++) {
      for (let k = j + 1; k < odd.length; k++) {
        if (isPrime(odd[i] + odd[j] + odd[k])) answer++;
      }
    }
  }
  odd.forEach((x, idx) => {
    for (let i = 0; i < even.length - 1; i++) {
      for (let j = i + 1; j < even.length; j++) {
        // console.log(x , even[i] , even[j])
        if (isPrime(x + even[i] + even[j])) answer++;
      }
    }
  });
  return answer;
}
