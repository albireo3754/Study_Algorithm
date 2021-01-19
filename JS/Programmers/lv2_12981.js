function solution(n, words) {
  var answer = [];
  const people = new Array(n + 1).fill(0);
  const wordSet = new Set();
  let idx = 1;
  let before = words[0][0];
  for (let word of words) {
    people[idx] += 1;
    if (wordSet.has(word) || before[before.length - 1] !== word[0]) {
      return [idx, people[idx]];
    }
    wordSet.add(word);
    before = word;
    if (++idx === n + 1) idx = 1;
  }
  return [0, 0];
}
