#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int T;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> T;
    while (T--) {
        string s;
        int k;
        vector<int> chars[26];

        cin >> s;
        cin >> k;
        
        for (int length = 0; length < s.size(); ++length)
            {
                chars[s[length] - 'a'].push_back(length);
            }

        int maxResult = -1, minResult = 100001;
        for (const auto& v: chars) {
            if (v.size() < k) {
                continue;
            }
            int index = 0;
            while (index + k - 1 < v.size()) {
                maxResult = max(maxResult, v[index + k - 1] - v[index] + 1);
                minResult = min(minResult, v[index + k - 1] - v[index] + 1);
                index++;
            }
        }
        if (maxResult == -1) {
            cout << -1 << "\n";
        } else {
            cout << minResult << " " << maxResult << "\n";
        }
    }
}
