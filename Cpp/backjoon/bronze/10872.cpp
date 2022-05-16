#include <stdio.h>

int main() {
  int N;
  scanf("%d", &N);
  int fact = 1;
  for (int i = 1; i <= N; i++)
  { 
    fact *= i;
  }
  printf("%d", fact);
  return 0;
}