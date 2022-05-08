#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int a, b, c, d;
    bool sieve[10][10][10][10] = { false };
    cin >> a >> b >> c >> d;
    string s = to_string(a) + to_string(b) + to_string(c) + to_string(d);
    vector<int> v;
    for (int i = 0; i < 4; i++) {
        char first = s.front();
        s = s.substr(1) + first;
        v.push_back(stoi(s));
    }
    sort(v.begin(), v.end());
    int N = v.front();
    int result = 1;
    int start = 1111;
    // cout << N;
    while (start < N) {
        string temp = to_string(start);
        start++;

        if (temp.find("0") != string::npos) {
            continue;
        }
        if (sieve[temp[0] - '0'][temp[1] - '0'][temp[2] - '0'][temp[3] - '0']) {
            continue;
        }
        
        for (int i = 0; i < 4; i++) {
            char first = temp.front();
            temp = temp.substr(1) + first;
            sieve[temp[0] - '0'][temp[1] - '0'][temp[2] - '0'][temp[3] - '0'] = true;
        }
        result++;
    }
    cout << result;
    return 0;
}