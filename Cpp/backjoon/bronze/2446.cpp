#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    int i = 2 * N - 1;
    int j = 0;
    while (i >= 1)
    {
        
        for (int k = 0; k < j; k++) {
            printf(" ");
        }
        for (int k = 0; k < i; k++) {
            printf("*");
        }
        printf("\n");
        j += 1;
        i -= 2;
    }

    j -= 1;
    i += 2;
    while (i < 2 * N - 1)
    {
        j -= 1;
        i += 2;
        for (int k = 0; k < j; k++) {
            printf(" ");
        }
        for (int k = 0; k < i; k++) {
            printf("*");
        }
        printf("\n");
    }
}