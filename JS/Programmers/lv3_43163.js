function check(str1, str2) {
  let correct = 0;
  for (let i = 0; i < str1.length; i++) {
    if (str1[i] !== str2[i]) correct++;
  }
  return correct === 1 ? true : false;
}

function solution(begin, target, words) {
  const wordMap = new Map(words.map((word) => [word, []]));
  wordMap.set(begin, []);
  for (let i = 0; i < words.length; i++) {
    for (let j = i + 1; j < words.length; j++) {
      if (check(words[i], words[j])) {
        wordMap.get(words[i]).push(words[j]);
        wordMap.get(words[j]).push(words[i]);
      }
    }
    if (check(begin, words[i])) {
      wordMap.get(begin).push(words[i]);
    }
  }
  console.log([...wordMap]);
  const track = [];
  let answer = 50;
  let hasTrack = false;
  function dfs(word, visited) {
    if (word === target) {
      answer = Math.min(track.length, answer);
      hasTrack = true;
    }
    if (track.length === words.length) return;
    // not yet find
    // clear
    console.log(word, 'dfs');
    for (let i of wordMap.get(word)) {
      // console.log(i, 'prune')
      if (track.indexOf(i) >= 0) continue;
      // console.log(wordMap.get(i))
      track.push(i);
      dfs(i, visited);
      track.pop(i);
    }
  }
  dfs(begin, new Set());
  return hasTrack ? answer : 0;
}
