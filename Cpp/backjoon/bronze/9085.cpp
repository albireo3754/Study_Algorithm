#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        int N;
        scanf("%d", &N);
        string s;
        int total = 0;
        for (int j = 0; j < N; j++) {
            cin >> s;
            total += stoi(s);
        }
        cout << total << endl;
        
    }
    return 0;
}