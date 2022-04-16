#include <iostream>
#include <cmath>

using std::cout;
using std::cin;
using std::endl;

bool isSquare(int num) {
  return true;
}

int main() {
  int M, N;
  cin >> M;
  cin >> N;

  int min = -1;
  int sum = 0;
  for(int i = ceil(sqrt(M)); i <= sqrt(N); i++) {
    if (min == -1) {
      min = pow(i, 2);
    }
    sum += pow(i, 2);
  }
  if (min == -1) {
    cout << min << endl;
  } else {
    cout << sum << endl;
    cout << min << endl;
  }  
  return 0;
}