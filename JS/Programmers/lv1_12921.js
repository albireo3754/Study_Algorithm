function solution(n) {
    const sieve = [];
    for (let i = 0; i < n + 1; i++) {
        sieve.push(i);
    }
    const primes = [];

    for (let j = 2; j < sieve.length; j++) {
        if (sieve[j] === -1) continue; 
        primes.push(j);
        let nonPrime = j;
        while (nonPrime < sieve.length) {
            sieve[nonPrime] = -1;
            nonPrime += j;
        }
    }
    return primes.length;
}
