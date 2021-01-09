//1 . 37% -> typo problem
//2. 100%

// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');
function solution(S, P, Q) {
  // write your code in JavaScript (Node.js 8.9.4)
  var as=new Array(S.length+1).fill(0);
  var cs=new Array(S.length+1).fill(0);
  var gs=new Array(S.length+1).fill(0);
  var ts=new Array(S.length+1).fill(0);
  var a =0 ;
  var c =0 ;
  var g =0 ;
  var t =0 ;
  var impactNumbers = new Array(P.length);

  
  for(var idx=0; idx<S.length; idx++){
    switch(S[idx]){
      case 'A' :
          ++a;
          break;
      case 'C' :
          ++c;
          break;
      case 'G' :
          ++g;
          break;
      case 'T' :
          ++t;
          break;
    } 
    as[idx+1] = a;
    cs[idx+1] = c;
    gs[idx+1] = g;
    ts[idx+1] = t;
  }

    
  for(var idx =0; idx<P.length; idx++){
    if (as[P[idx]] < as[Q[idx]+1]){
      impactNumbers[idx] = 1;
    }
    else if (cs[P[idx]] < cs[Q[idx]+1]){
      impactNumbers[idx] = 2;
    }
    else if (gs[P[idx]] < gs[Q[idx]+1]){
      impactNumbers[idx] = 3;
      
    }
    else{
      impactNumbers[idx] = 4;
    }
  
  }
  
  return impactNumbers;

}