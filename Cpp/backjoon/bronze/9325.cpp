#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        int price;
        int optionCount;
        scanf("%d", &price);
        scanf("%d", &optionCount);
        for (; optionCount > 0; optionCount--) {
            int q, p;
            scanf("%d %d", &q, &p);
            price += q * p;
        }
        printf("%d\n", price);
    }
    return 0;
}