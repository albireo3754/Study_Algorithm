function solution(s) {
  return s
    .split(" ")
    .map((x) => {
      let wordSum = "";
      for (let i = 0; i < x.length; i++) {
        if (i % 2 === 0) wordSum += x[i].toUpperCase();
        else wordSum += x[i].toLowerCase();
      }
      return wordSum;
    })
    .join(" ");
}
