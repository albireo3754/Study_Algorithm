#include <stdio.h>

int n;

struct People {
  char name[101];
  int dd;
  int mm;
  int yyyy;
};
int main() {
  People maxPeople;
  People minPeople;
  scanf("%d", &n);
  
  for (int i = 0; i < n; i++) {
    People tempPeople;
    scanf("%s %d %d %d", tempPeople.name, &tempPeople.dd, &tempPeople.mm, &tempPeople.yyyy);  
    if (i == 0) {
      maxPeople = tempPeople;
      minPeople = tempPeople;
    } else {
      if (tempPeople.yyyy < maxPeople.yyyy || 
      (tempPeople.yyyy == maxPeople.yyyy && tempPeople.mm < maxPeople.mm) ||
      (tempPeople.yyyy == maxPeople.yyyy && tempPeople.mm == maxPeople.mm && tempPeople.dd < maxPeople.dd)) {
        maxPeople = tempPeople;
      }
      if (minPeople.yyyy < tempPeople.yyyy || 
      (minPeople.yyyy == tempPeople.yyyy && minPeople.mm < tempPeople.mm) ||
      (minPeople.yyyy == tempPeople.yyyy && minPeople.mm == tempPeople.mm && minPeople.dd < tempPeople.dd)) {
        minPeople = tempPeople;
      }
    }
  } 
  printf("%s\n%s", minPeople.name, maxPeople.name); 
  return 0;
}