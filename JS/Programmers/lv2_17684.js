function solution(msg) {
  const dict = new Map(
    [
      "A",
      "B",
      "C",
      "D",
      "E",
      "F",
      "G",
      "H",
      "I",
      "J",
      "K",
      "L",
      "M",
      "N",
      "O",
      "P",
      "Q",
      "R",
      "S",
      "T",
      "U",
      "V",
      "W",
      "X",
      "Y",
      "Z"
    ].map((x, i) => {
      return [x, i + 1];
    })
  );
  let index = 0;
  const answer = [];
  let dictIdx = 27;
  if (dict.get(msg)) return [dict.get(msg)];
  while (index < msg.length) {
    let char = msg[index];
    for (let i = index + 1; i < msg.length; i++) {
      let wc = char + msg[i];
      if (i === msg.length - 1) {
        if (dict.has(wc)) answer.push(dict.get(wc));
        else {
          answer.push(dict.get(char));
          answer.push(dict.get(msg[i]));
        }
        return answer;
      }
      if (!dict.has(wc)) {
        dict.set(wc, dictIdx++);
        // index추가
        index = i;
        break;
      }
      char = wc;
    }
    answer.push(dict.get(char));
  }
  console.log(answer);
  // return answer;
}
