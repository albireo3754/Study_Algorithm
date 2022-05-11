#include <stdio.h>
#include <iostream>
int main() {
    int N;
    scanf("%d", &N);
    int total = 0;
    int temp = 0;
    for (int i = 0; i < N; i++) {
        int T;
        std::cin >> T;
        if (T == 1) {
            temp++;
        } else {
            temp = 0;
        }
        total += temp;
    }
    printf("%d", total);
    return 0;
}