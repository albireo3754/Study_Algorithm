#include <iostream>

using namespace std;

int N;
int boxs[1001];
int dp[1001] = {};
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    memset(dp, 1, 1001);

    cin >> N;

    for (int n = 0; n < N; ++n)
    {
        cin >> boxs[n];
    }

    int result = 0;
    for (int n = 0; n < N; ++n)
    {
        int box = boxs[n];
        dp[n] = 1;
        for (int j = 0; j < n; ++j)
        {
            int cmpBox = boxs[j];
            if (cmpBox < box)
            {
                dp[n] = max(dp[n], dp[j] + 1);
            }
        }
        result = max(result, dp[n]);
    }

    cout << result;

    return 0;
}