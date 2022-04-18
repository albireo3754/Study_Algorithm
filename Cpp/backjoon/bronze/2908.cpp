#include <iostream>

using namespace std;

char* reverse(const char* arr) {
  char* result;
  for(int i = 0, j = 2; i < 3; i++, j--) {
    result[i] = arr[j];
  }
  return result;
}

int main() {
  char A[4], B[4];
  cin >> A >> B;
  char result[3];
  for(int i = 0, j = 2; i < 3; i++, j--) {
    if (A[j] < B[j]) {
      cout << B[2] << B[1] << B[0];
      return 0;
    } else if (A[j] > B[j]) {
      cout << A[2] << A[1] << A[0];
      return 0;
    }
  }
  cout << A[2] << A[1] << A[0];
  return 0;
}