#include <iostream>
#include <algorithm>

using namespace std;
int N, K;
int result = 0;
int d = 1'000'000'000;

// N, K의 서브배열
long long int dp[201][201];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> K;

    // for (int n = 0; n <= N; ++n)
    // {
    // dp[0][n] =
    // }
    // <= N 까지의 범위를 구하기
    for (int i = 0; i <= N; i++)
    {
        dp[1][i] = 1;
    }

    for (int k = 1; k <= K; k++)
    {
        for (int n = 0; n <= N; n++)
        {
            for (int i = 0; i <= n; i++)
            {
                // dp[4][20]을 구하기 위해선 3번 더해서 0 ~ 20 까지 만드는 합을 다 더해주면된다.
                // 처음엔 n번 더하는 경우까지 모두 포함했는데 결국 이전 점화식에 다 포함되는 내용이였음
                dp[k][n] = dp[k][n] % d + dp[k - 1][n - i] % d;
            }
        }
    }

    // for (int n = 0; n <= N; n++)
    // {
    //     for (int j = 0; j <= N; j++)
    //     {
    //         cout << dp[n][j] << ' ';
    //     }
    //     cout << '\n';
    // }

    cout << dp[K][N];

    return 0;
}