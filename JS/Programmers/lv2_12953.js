//num1 > num2;
function gcd(num1, num2) {
  while (num2 !== 0) {
    [num1, num2] = [num2, num1 % num2];
  }
  return num1;
}
function solution(arr) {
  let sortedArr = [...arr].sort((a, b) => b - a);
  let lcm = sortedArr[0];
  for (let i = 1; i < arr.length; i++) {
    lcm = (lcm * sortedArr[i]) / gcd(lcm, sortedArr[i]);
  }
  return lcm;
}
