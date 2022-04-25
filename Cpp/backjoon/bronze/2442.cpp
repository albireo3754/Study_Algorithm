#include <stdio.h>

int main() {
  int N;
  scanf("%d", &N);

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N - 1 - i; j++) {
      printf(" ");
    }
    for (int j = 0; j < i * 2 + 1; j++) {
      printf("*");
    }
    printf("\n"); 
  }
}