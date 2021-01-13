function solution(people, limit) {
  const peopleSorted = [...people].sort((a, b) => a - b);
  let answer = 0;
  while (peopleSorted.length !== 0) {
    let weightLeft = limit - peopleSorted.pop();
    if (weightLeft >= peopleSorted[0]) {
      peopleSorted.shift();
    }
    answer += 1;
  }
  return answer;
}

// shift function is O(n). If i use twopointer, i can improve velocity. But i don't know that need.
