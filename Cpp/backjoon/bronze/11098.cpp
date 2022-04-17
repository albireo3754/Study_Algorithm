#include <iostream>
#include <string.h>
using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    int P;
    int maxC = -1;
    char maxName[21];
  
    cin >> P;
    for (int j = 0; j < P; j++) {
      int tempC;
      char tempName[21]; 
      cin >> tempC >> tempName;
      if (maxC < tempC) {
        maxC = tempC;
        strcpy(maxName, tempName);
      }
    }
    cout << maxName << endl;
  }
  return 0;
}