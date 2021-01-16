function sum(arr) {
  return arr.reduce((acc, cur) => acc + cur);
}

function solution(arr) {
  const answer = [0, 0];
  function quad(arr_, n) {
    let quadsum = sum(arr_.flat());
    if (quadsum === n ** 2) answer[1] += 1;
    else if (quadsum === 0) answer[0] += 1;
    else {
      // [arr_[0][:half] , .... , arr_[half][:half]]
      let arr_1 = [];
      for (let i = 0; i < n / 2; i++) {
        arr_1.push(arr_[i].slice(0, n / 2));
      }
      quad(arr_1, n / 2);
      // arr_2 [arr_[0][half:]]
      let arr_2 = [];
      for (let i = 0; i < n / 2; i++) {
        arr_2.push(arr_[i].slice(n / 2));
      }
      quad(arr_2, n / 2);
      // arr_3
      let arr_3 = [];
      for (let i = n / 2; i < n; i++) {
        arr_3.push(arr_[i].slice(0, n / 2));
      }
      quad(arr_3, n / 2);
      // arr_4
      let arr_4 = [];
      for (let i = n / 2; i < n; i++) {
        arr_4.push(arr_[i].slice(n / 2));
      }
      quad(arr_4, n / 2);
    }
  }
  quad(arr, arr.length);
  return answer;
}
