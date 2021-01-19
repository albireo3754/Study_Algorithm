function solution(files) {
  const splitFile = files.map((file) => {
    let headTail = file.match(/[0-9]/).index;
    let numberTail = file.match(/[0-9][^0-9]/i)
      ? file.match(/[0-9][^0-9]/).index + 1
      : file.length;
    return [
      file.slice(0, headTail),
      file.slice(headTail, numberTail),
      file.slice(numberTail),
    ];
  });
  splitFile.sort((a, b) => {
    if (a[0].toLowerCase() > b[0].toLowerCase()) {
      return 1;
    } else if (a[0].toLowerCase() < b[0].toLowerCase()) {
      return -1;
    } else {
      return Number(a[1].slice(0, 5)) - Number(b[1].slice(0, 5));
    }
  });
  console.log(splitFile);
  return splitFile.map((x) => x.join(''));
}
