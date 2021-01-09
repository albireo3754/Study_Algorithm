function solution(s) {
  let answer = s.length;
  if (answer === 1) return 1;
  for (let repeat = 1; repeat <= s.length / 2 + 1; repeat += 1) {
    const sliceArray = [];
    for (let i = 0; i < s.length; i += repeat) {
      sliceArray.push(s.slice(i, i + repeat));
    }
    let compressed = '';
    let cnt = 0;
    for (let pattern = 0; pattern < sliceArray.length; pattern += 1) {
      if (pattern === sliceArray.length - 1) {
        compressed += sliceArray[pattern];
      }
      for (let compare = pattern; compare < sliceArray.length; compare += 1) {
        if (compare === sliceArray.length - 1) {
          if (sliceArray[pattern] === sliceArray[compare]) {
            cnt += 1;
            compressed +=
              cnt - 1 ? `${cnt}${sliceArray[pattern]}` : sliceArray[pattern];
          } else {
            compressed +=
              cnt - 1
                ? `${cnt}${sliceArray[pattern]}${sliceArray[compare]}`
                : `${sliceArray[pattern]}${sliceArray[compare]}`;
          }
          pattern = compare;
          break;
        }

        if (sliceArray[pattern] === sliceArray[compare]) {
          cnt += 1;
        } else {
          compressed +=
            cnt - 1 ? `${cnt}${sliceArray[pattern]}` : sliceArray[pattern];
          pattern = compare - 1;
          cnt = 0;
          break;
        }
      }
    }
    const compLength = compressed.length;
    if (answer > compLength && compLength > 0) {
      answer = compLength;
    }
  }
  return answer;
}

// 정규식으로인한 replace all 함수는 10, 이상의 1을 전부 없애버렸음 ㅠㅠ

// function solution(s) {
//   let answer = 1001;
//   for (let repeat = 1; repeat <= parseInt(s.length / 2); repeat += 1) {
//     let pattern = s.slice(0, repeat);
//     let idx = repeat;
//     let compressed = '';
//     let cnt = 1;
//     while (idx < s.length) {
//       const isCompare = s.slice(idx, idx + repeat);
//       if (pattern === isCompare) {
//         cnt += 1;
//       } else if (pattern !== isCompare) {
//         compressed += `${cnt}${pattern}`;
//         cnt = 1;
//       }
//       if (idx >= s.length - repeat) {
//         if (cnt === 1) compressed += isCompare;
//         else compressed += `${cnt}${pattern}`;
//       }
//       pattern = isCompare;
//       idx += repeat;
//     }

//     const compLength = compressed.replace(/1/g, '').length;
//     if (answer > compLength) {
//       answer = compLength;
//     }
//   }

//   return answer;
// }

// solution('abc');
