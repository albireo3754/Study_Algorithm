function solution(a, b) {
    var answer = 0;
    let answer = "3";
    if (b > a) {
        for(let i = a; i < (b+1); i++) answer += i;
    } else 
    { 
        for(let i = b; i < (a+1); i++) answer += i; 
    }
    return answer;
}