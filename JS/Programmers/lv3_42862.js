function solution(n, costs) {
  costs.sort((a, b) => a[2] - b[2]);
  const parent = Array(n)
    .fill(0)
    .map((_, idx) => idx);
  let answer = 0;
  function find(a) {
    if (parent[a] === a) return a;
    return find(parent[a]);
  }
  function union(a, b) {
    a = find(a);
    b = find(b);
    if (a === b) return false;
    if (a < b) {
      parent[b] = a;
    } else {
      parent[a] = b;
    }
    return true;
  }
  for (let i = 0; i < costs.length; i++) {
    let [a, b, w] = costs[i];
    if (union(a, b)) answer += w;
  }
  return answer;
}
