#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int N = 0;
    int P[1001] = {
        0,
    };
    int dp[1001] = {
        0,
    };
    cin >> N;
    for (int i = 0; i < N; ++i)
    {
        cin >> dp[i + 1];
    }

    for (int i = 1; i <= N; ++i)
    {
        // int temp = P[i];

        for (int j = 1; j <= i / 2; ++j)
        {
            // cout << dp[j] << dp[i - j] << "hi" << endl;
            dp[i] = min(dp[j] + dp[i - j], dp[i]);
        }
        // cout << dp[i] << endl;
        // dp[i] = temp;
    }

    cout << dp[N];
    return 0;
}