#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string s1;
string s2;
string s3;

int result = 0;
int dp[101][101][101] = {};

int main()
{
    cin >> s1 >> s2 >> s3;

    for (int i = 0; i < (int)s1.length(); ++i)
    {
        for (int j = 0; j < (int)s2.length(); ++j)
        {
            for (int k = 0; k < s3.length(); ++k)
            {
                if (s1[i] == s2[j] && s1[i] == s3[k])
                {
                    dp[i + 1][j + 1][k + 1] = dp[i][j][k] + 1;
                }
                else
                {

                    dp[i + 1][j + 1][k + 1] = max(dp[i + 1][j + 1][k], dp[i + 1][j][k + 1]);
                    dp[i + 1][j + 1][k + 1] = max(dp[i + 1][j + 1][k + 1], dp[i][j + 1][k + 1]);
                }
                result = max(result, dp[i + 1][j + 1][k + 1]);
            }
        }
    }

    cout << result;
}
