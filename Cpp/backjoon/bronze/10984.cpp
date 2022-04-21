#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        int N;
        scanf("%d", &N);
        int totalC = 0;
        float totalG = 0;
        for (int j = 0; j < N; j++) {
            float G;
            int C;
            scanf("%d %f", &C, &G);
            totalC += C;
            totalG += G * C;
        }
        printf("%d ", totalC);
        printf("%.1f\n", totalG / totalC);
    }
}