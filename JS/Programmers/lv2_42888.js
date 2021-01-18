function solution(record) {
  let answer = [];
  let id = new Map();
  record.forEach((str) => {
    let strArr = str.split(' ');
    if (strArr[0] === 'Enter') {
      id.set(strArr[1], strArr[2]);
      answer.push([strArr[1], '님이 들어왔습니다.']);
    } else if (strArr[0] === 'Leave') {
      answer.push([strArr[1], '님이 나갔습니다.']);
    } else {
      id.set(strArr[1], strArr[2]);
    }
  });
  return answer.map((x) => id.get(x[0]) + x[1]);
}
