#include <stdio.h>

int main() {
    int total;
    scanf("%d", &total);

    for (int i = 0; i < 9; i++) {
        int book;
        scanf("%d", &book);
        total -= book;
    }
    printf("%d", total);
}