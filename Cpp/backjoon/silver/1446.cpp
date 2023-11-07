#include <iostream>
#include <algorithm>

using namespace std;

int N, D;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> D;

    int a, b, c;
    vector<vector<int>> as;
    for (int n = 0; n < N; ++n)
    {
        cin >> a >> b >> c;
        as[n][0] = a;
        as[n][1] = b;
        as[n][2] = c;
    }

    sort(as.begin(), as.end());
    int result = D;
    for (int i = 0; i < (1 << (N)); ++i)
    {
        int before = 0;
        int temp = 0;
        for (int n = 0; n < N; ++n)
        {
            if (i & (1 << n) && as[n][0] >= before)
            {
                temp += as[n][0] - before + as[n][2];
                before = as[n][1];
            }
        }
        result = min(result, temp);
    }
    cout << result;
    return 0;
}
