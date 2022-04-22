#include <stdio.h>

int main() {
  int N;
  scanf("%d", &N);
  int result = 0;
  for (int i = 0; i < N; i++) {
    int student, apple;
    scanf("%d %d", &student, &apple);
    result += apple % student;
  }  
  printf("%d", result);
}