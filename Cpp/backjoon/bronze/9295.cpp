#include <stdio.h>

int main() {
  int T;

  scanf("%d", &T);

  for (int i = 0; i < T; i++) {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("Case %d: %d\n", i, a+b);
  }  
  return 0;
}