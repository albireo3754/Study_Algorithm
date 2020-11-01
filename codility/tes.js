function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  var cars = -1e
  var count = 0;
  var pairsOfPassingCars = 0;w Array(A.length).fill(0);
  for(var idx= 0; idx < A.length; idx++){
    if(A[idx] === 0){
      pairsOfPassingCars += (A[idx] - east + 1) * count
      count += 1;
      east = A[idx]
    }
  }
  return pairsOfPassingCars;
}
      minIdx = idx - 1;
    }
    if (minValue > minThree) {
      minValue = minThree;
      minIdx = idx - 2;
    }
  }
  return minIdx;
}

console.log(solution([4, 2, 2, 5, 1, 5, 8]));
