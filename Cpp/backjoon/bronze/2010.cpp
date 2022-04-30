#include <stdio.h>

int main() {
  int N;
  scanf("%d", &N);
  int computer_count = 1;
  for (int i = 0; i < N; i++) {
    int plug_count;
    scanf("%d", &plug_count);
    computer_count--;
    computer_count += plug_count;
  }
  printf("%d", computer_count);
}