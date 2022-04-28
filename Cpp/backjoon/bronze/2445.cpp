#include <stdio.h>

void print(int base, int star) {
    for (int i = 0; i < star; i++) {
        printf("*");
    }

    for (int i = 0; i < 2 * (base - star); i++) {
        printf(" ");
    }

    for (int i = 0; i < star; i++) {
        printf("*");
    }

    printf("\n");
}

int main() {
    int N;
    scanf("%d", &N);
    for (int i = 1; i <= N; i++) {
        print(N, i);
    }
    
    for (int i = N - 1; i >= 1; i--) {
        print(N, i);
    }
    return 0;
}