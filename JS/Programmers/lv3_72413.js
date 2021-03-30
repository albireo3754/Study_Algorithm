// function solution(n, s, a, b, fares) {
//   // [[] for i in range(N + 1)]
//   const Inf = 9999999999;
//   const edge = Array(n + 1)
//     .fill(0)
//     .map((x) => Array(n + 1).fill(Inf));
//   for (let [a, b, v] of fares) {
//     edge[a][b] = v;
//     edge[b][a] = v;
//   }
//   // for (let i of edge) console.log(i)
//   for (let k = 1; k <= n; k++) {
//     for (let i = 1; i <= n; i++) {
//       for (let j = 1; j <= n; j++) {
//         if (i == j) {
//           edge[i][i] = 0;
//           continue;
//         }
//         if (edge[i][k] === Inf || edge[k][j] === Inf) continue;
//         if (edge[i][j] > edge[i][k] + edge[k][j]) {
//           edge[i][j] = edge[i][k] + edge[k][j];
//         }
//       }
//     }
//   }
//   console.log(edge);
//   const answer = edge[s].reduce((acc, cur, idx) => {
//     if (acc > cur + edge[idx][a] + edge[idx][b]) {
//       return cur + edge[idx][a] + edge[idx][b];
//     }
//     return acc;
//   }, Inf);

//   return answer;
// }
class Heapq {
  constructor() {
    this.q = [];
    this.n = 0;
  }

  heappush(i) {
    this.q.push(i);
    this.n++;
    if (this.n === 1) {
      return;
    }
    let right = this.n - 1;
    let left = Math.floor(this.n / 2) - 1;

    while (left >= 0 && right > 0) {
      if (this.q[right][0] >= this.q[left][0]) {
        return;
      }
      console.log(left, right);

      [this.q[left], this.q[right]] = [[...this.q[right]], [...this.q[left]]];

      [left, right] = [Math.floor((left - 1) / 2), left];
    }
  }
}

const q = new Heapq();
q.heappush([1, 2]);
q.heappush([3, 2]);
q.heappush([2, 2]);
q.heappush([1, 2]);
console.log(q.q);

class Heapq {
  constructor() {
    this.q = [];
    this.length = 0;
  }

  heappush(i) {
    this.q.push(i);
    this.length++;
    if (this.length === 1) {
      return;
    }
    let right = this.length - 1;
    let left = Math.floor(this.length / 2) - 1;

    while (left >= 0 && right > 0) {
      if (this.q[right][0] >= this.q[left][0]) {
        return;
      }
      [this.q[left], this.q[right]] = [this.q[right], this.q[left]];
      [left, right] = [Math.floor((left - 1) / 2), left];
    }
  }

  heappop() {
    [this.q[0], this.q[this.length - 1]] = [this.q[this.length - 1], this.q[0]];
    let left = 0;
    let right = left * 2 + 1;
    while (right + 1 < this.length - 1) {
      if (
        this.q[left][0] < this.q[right][0] &&
        this.q[left][0] < this.q[right + 1][0]
      ) {
        break;
      }
      if (this.q[right][0] > this.q[right + 1][0]) {
        right += 1;
      }
      [this.q[left], this.q[right]] = [this.q[right], this.q[left]];
      [left, right] = [right, right * 2 + 1];
    }
    if (right < this.length - 1 && this.q[left][0] > this.q[right][0]) {
      [this.q[left], this.q[right]] = [this.q[right], this.q[left]];
    }
    this.length--;
    return this.q.pop();
  }
}

function solution(n, s, a, b, fares) {
  const Inf = 9999999999;
  const edge = Array(n + 1)
    .fill(0)
    .map((x) => []);
  for (let [a, b, v] of fares) {
    edge[a].push([b, v]);
    edge[b].push([a, v]);
  }

  const dijkstra = (i) => {
    const dist = Array(n + 1).fill(Inf);
    const q = new Heapq();
    q.heappush([0, i]);
    dist[i] = 0;

    while (q.length > 0) {
      let [v, here] = q.heappop();
      if (dist[here] < v) continue;
      for (let [there, w] of edge[here]) {
        if (dist[there] > dist[here] + w) {
          dist[there] = dist[here] + w;
          q.heappush([dist[there], there]);
        }
      }
    }
    return dist;
  };
  // console.log(dijkstra(2));

  const costs = dijkstra(s).map((v, i) => {
    const duo = dijkstra(i);
    return v + duo[a] + duo[b];
  });
  console.log(costs);
  return Math.min(...costs);
}
