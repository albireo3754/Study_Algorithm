#include <iostream>
#include <string>

using namespace std;
int dp[4001][4001] = {};
int result = 0;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    string s1;
    string s2;

    cin >> s1 >> s2;

    for (int i = 1; i <= s1.size(); ++i)
    {

        for (int j = 1; j <= s2.size(); ++j)
        {
            if (s1[i - 1] == s2[j - 1])
            {
                dp[i][j] = dp[i - 1][j - 1] + 1;
                result = max(result, dp[i][j]);
            }
        }
    }

    cout << result;

    return 0;
}