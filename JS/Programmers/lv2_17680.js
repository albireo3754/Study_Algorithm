function solution(cacheSize, cities) {
  let cache = [];
  // if (cacheSize === 0) return
  let answer = cities
    .map(x => x.toLowerCase())
    .reduce((acc, city) => {
      let idx = cache.indexOf(city);
      if (cache.length < cacheSize) {
        if (idx === -1) {
          cache.push(city);
          return acc + 5;
        }
        {
          cache.splice(idx, 1);
          cache.push(city);
          return acc + 1;
        }
      }
      if (idx === -1) {
        cache.push(city);
        cache.shift();
        return acc + 5;
      } else {
        cache.splice(idx, 1);
        cache.push(city);
        return acc + 1;
      }
    }, 0);
  return answer;
}
