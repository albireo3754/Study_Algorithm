#include <iostream>
#include <algorithm>

using namespace std;

int N;
pair<int, int> reservations[16];
int dp[16] = {};
int main()
{
    cin >> N;

    int period;
    int price;
    int result = 0;
    for (int n = 0; n < N; ++n)
    {
        cin >> period >> price;
        reservations[n] = make_pair(period, price);
    }

    for (int n = 0; n < N; ++n)
    {
        auto [period, price] = reservations[n];
        for (int j = n + period; j <= N; ++j)
        {
            dp[j] = max(dp[j], dp[n] + price);
            result = max(result, dp[j]);
        }
    }

    // for (int i = 0; i < N; ++i)
    // {
    //     cout << dp[i] << " , ";
    // }

    cout << result;

    return 0;
}