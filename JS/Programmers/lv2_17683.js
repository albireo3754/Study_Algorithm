function solution(m, musicinfos) {
  // start, end, name, music = musicinfo;
  const processing = [];
  for (let musicinfo of musicinfos) {
    let [start, end, name, music] = musicinfo.split(',');
    let newMusic = music
      .replace(/C#/g, 'c')
      .replace(/D#/g, 'd')
      .replace(/F#/g, 'f')
      .replace(/A#/g, 'a')
      .replace(/G#/g, 'g');
    console.log(newMusic);
    let h = 0;
    let min = 0;
    // 00:00 안넘기니간 h는안바꿔도? 문제오류나면 이거씀
    // if (end.slice(0, 2) < start.slice(0, 2)) {
    //     end.slice(0, 2) - start.slice(0, 2) + 24
    // }
    h = end.slice(0, 2) - start.slice(0, 2);
    if (end.slice(3) < start.slice(3)) {
      h--;
      min += 60;
    }
    min += end.slice(3) - start.slice(3);
    min += h * 60;
    console.log(min);
    let arr = [];
    for (let i = 0; i < min; i++) {
      arr.push(newMusic[i % newMusic.length]);
    }
    processing.push(arr.join(''));
  }
  const reg = new RegExp(
    m
      .replace(/C#/g, 'c')
      .replace(/D#/g, 'd')
      .replace(/F#/g, 'f')
      .replace(/A#/g, 'a')
      .replace(/G#/g, 'g')
  );
  let result = '';
  let resultIdx = -1;
  // console.log(processing)
  processing.forEach((x, i) => {
    if (x.match(reg)) {
      // console.log(x.match(reg))
      if (result.length < x.length) {
        result = x;
        resultIdx = i;
      }
    }
  });
  // console.log(resultIdx);
  return resultIdx === -1 ? '(None)' : musicinfos[resultIdx].split(',')[2];
}
