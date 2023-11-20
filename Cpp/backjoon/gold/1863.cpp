#include <iostream>
#include <algorithm>
#include <set>
#include <stack>

using namespace std;
int N;
vector<pair<int, int>> v{};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    stack<int> s = {};
    cin >> N;
    int x, y;
    int result = 0;
    for (int n = 0; n < N; ++n)
    {
        cin >> x >> y;
        v.emplace_back(x, y);
    }

    sort(v.begin(), v.end());

    for (int n = 0; n < N; ++n)
    {
        auto [x, y] = v[n];
        if (y == 0)
        {
            s = {};
            continue;
        }

        while (!s.empty() && s.top() > y)
        {
            s.pop();
        }
        if (s.empty() || s.top() != y)
        {
            //             cout << x << " " << y << "\n";
            result++;
        }
        s.push(y);
    }

    // for (int i = 0; i < N; ++i)
    // {
    //     cout << v[i].first << " " << v[i].second << "\n";
    // }

    cout << result;

    return 0;
}
