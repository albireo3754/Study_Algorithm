#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
    {
        int V, E;
        scanf("%d %d", &V, &E);
        printf("%d\n", 2 - V + E);
    }
}