#include <iostream>
int N;
int dp[31] = {1, 0, 3, 0, 11};
int main()
{
    using namespace std;

    cin >> N;

    switch (N)
    {
    case 1:
    {
        cout << 0;
        return 0;
    }
    case 2:
        cout << 3;
        return 0;
    }

    if (N % 2 == 1)
    {
        cout << 0;
        return 0;
    }

    for (int i = 4; i <= N; i = i + 2)
    {
        dp[i] = dp[i - 2] * dp[2];
        for (int j = 4; j <= i; j = j + 2)
        {
            dp[i] += dp[i - j] * 2;
        }
    }
    cout << dp[N];
}