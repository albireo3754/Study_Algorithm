#include <iostream>
using namespace std;

int dp[15][15] = {
    0,
};

int main()
{
    int T, k, n;

    cin >> T;

    for (int y = 1; y < 15; ++y)
    {
        dp[0][y] = y;
    }
    for (int i = 1; i < 15; ++i)
    {
        for (int y = 1; y < 15; ++y)
        {
            dp[i][y] = dp[i][y - 1] + dp[i - 1][y];
        }
    }

    while (T--)
    {
        cin >> k >> n;
        cout << dp[k][n] << endl;
    }

    return 0;
}