#include <iostream>

using namespace std;

int main()
{
    int N;

    cin >> N;

    long long dp[100001] = {1, 0, 1, 0, 2};

    for (int i = 6; i <= N; i = i + 2)
    {
        long long temp = 0;
        for (int j = 0; j < i; j = j + 2)
        {
            temp += ((dp[j] * dp[i - 2 - j]));
            temp %= 987654321;
        }
        dp[i] = temp;
    }

    //    printf("%lld", dp[N]);
    cout << dp[N] << endl;
    return 0;
}
