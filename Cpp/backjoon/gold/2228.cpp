#include <iostream>
#include <algorithm>

using namespace std;
int N, M;
int arrs[101];
int dp[100][51];
int sum[101][101];
constexpr int inf = -999999999;

int sol(int n, int m)
{
    if (m == M)
    {
        return 0;
    }

    if (n >= N)
    {
        dp[n][m] = inf;
        return dp[n][m];
    }

    int &ret = dp[n][m];
    if (dp[n][m] != inf)
        return ret;

    ret = sol(n + 1, m);
    for (int i = n + 1; i < N + 1; i++)
    {
        ret = max(ret, sum[n][i] + sol(i + 1, m + 1));
    }
    return ret;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> N >> M;
    for (int n = 0; n < N; n++)
    {
        cin >> arrs[n];
    }
    fill(&dp[0][0], &dp[99][51], inf);
    // memset(dp, -1, size(dp));

    for (int n = 0; n < N; n++)
    {
        int s = arrs[n];
        for (int j = n + 1; j < N + 1; j++)
        {
            sum[n][j] = s;
            s += arrs[j];
        }
    }

    cout << sol(0, 0);

    // for (int n = 0; n < N; n++)
    // {
    //     for (int m = 0; m < N + 1; m++)
    //     {
    //         cout << dp[n][m] << " ";
    //         // cout << sum[n][m] << " ";
    //     }
    //     cout << "\n";
    // }
}