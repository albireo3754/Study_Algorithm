#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

constexpr int d = 1000000;
string code;
int dp[5001] = {};
int main()
{
    cin >> code;
    if (code.size() == 0)
    {
        cout << 0;
        return 0;
    }
    if (code[0] == '0')
    {
        cout << 0;
        return 0;
    }
    if (code.size() == 1)
    {
        if (code[0] != '0')
        {
            cout << 1;
        }
        return 0;
    }
    char buffer[2]{' ', code[0]};
    dp[0] = 1;
    dp[1] = 1;

    for (int i = 1; i < code.length(); ++i)
    {
        char c = code[i];

        int decoded = atoi(&c);

        buffer[0] = buffer[1];
        buffer[1] = c;

        // cout << buffer << "\n";
        int decoded2 = atoi(buffer);
        bool breakFlag = true;

        if (decoded2 >= 10 && decoded2 <= 26)
        {
            dp[i + 1] = (dp[i - 1]);
            breakFlag = false;
        }

        if (decoded == 0)
        {
            // fail
        }
        else
        {
            // codable
            dp[i + 1] = (dp[i + 1] + dp[i]) % d;
            breakFlag = false;
        }

        if (breakFlag)
        {
            cout << 0;
            return 0;
        }
    }
    cout << dp[code.length()];
    return 0;
}
