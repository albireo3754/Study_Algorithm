function solution(clothes) {
  let clothesType = new Map();
  clothes.forEach((clothing) => {
    if (clothesType.has(clothing[1])) {
      clothesType.get(clothing[1]).push(clothing[0]);
    } else {
      clothesType.set(clothing[1], [clothing[0]]);
    }
  });
  let answer = 1;
  for (let i of clothesType.values()) {
    answer *= i.length + 1;
  }
  return answer - 1;
}
