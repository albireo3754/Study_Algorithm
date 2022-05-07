#include <stdio.h>

int main() {
    int total = 0;
    int N;
    for (int i = 0; i < 5; i++) {
        scanf("%d", &N);
        total += N;
    }
    printf("%d", total);
}