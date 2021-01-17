function solution(str1, str2) {
  let answer = 0;
  const reg = /[a-z]{2}/gi;
  const map = new Map();
  let array1 = [...str1.slice(0, str1.length - 1)]
    .map((cur, idx) => {
      return cur + str1[idx + 1];
    })
    .map((a) => a.toUpperCase().replace(/[^A-Z]/g, ''))
    .filter((a) => a.length === 2);
  let array2 = [...str2.slice(0, str2.length - 1)]
    .map((cur, idx) => {
      return cur + str2[idx + 1];
    })
    .map((a) => a.toUpperCase().replace(/[^A-Z]/g, ''))
    .filter((a) => a.length === 2);
  array1.map((a) => {
    if (map.has(a)) map.set(a, [map.get(a)[0] + 1, map.get(a)[1]]);
    else map.set(a, [1, 0]);
  });
  array2.map((a) => {
    if (map.has(a)) map.set(a, [map.get(a)[0], map.get(a)[1] + 1]);
    else map.set(a, [0, 1]);
  });
  console.log(...map);

  function union() {
    let result = 0;
    for (let i of map) {
      result += Math.max(...i[1]);
    }
    return result;
  }
  function intersection() {
    let result = 0;
    for (let i of map) {
      result += Math.min(...i[1]);
    }
    return result;
  }
  answer = Math.floor((intersection() / union()) * 65536);
  return union() ? answer : 65536;
}
