function combi(arr) {
  const combiArr = [];
  function com(track) {
    if (track.length === arr.length) {
      combiArr.push(track);
      return;
    }
    for (let i = 0; i < arr.length; i++) {
      if (track.includes(arr[i])) continue;
      com([...track, arr[i]]);
    }
  }
  com([]);
  return combiArr;
}

function calc(num1, num2, op) {
  if (op === '*') return num1 * num2;
  else if (op === '+') return num1 + num2;
  return num1 - num2;
}
function solution(expression) {
  const operSets = [...new Set(expression.match(/[^0-9]/g))];
  let answer = 0;
  // console.log(nums);
  // console.log(operators);
  for (let operOrder of combi(operSets)) {
    // console.log(operOrder);
    function part(string, priorityIdx) {
      // console.log(string)
      const priority = operOrder[priorityIdx];
      let stringSplit = string.split(priority);
      // if (priorityIdx === operOrder.length) {
      //     return calc(...(stringSplit.map((n) => Number(n))), priority);
      // }
      // console.log(stringSplit, priority)
      if (stringSplit.length === 1) {
        if (stringSplit[0].match(/[^0-9]/)) {
          return part(string, ++priorityIdx);
        }
        return Number(stringSplit[0]);
      }
      let result = part(stringSplit[0], priorityIdx + 1);
      for (let i = 0; i < stringSplit.length - 1; i++) {
        result = calc(
          result,
          part(stringSplit[i + 1], priorityIdx + 1),
          priority
        );
      }
      console.log(result);
      return result;
    }
    //copy
    answer = Math.max(answer, Math.abs(part(expression.slice(0), 0)));
  }
  return answer;
}
