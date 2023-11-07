#include <iostream>
#include <string>

using namespace std;

string s;

int bCount(int i, int length)
{
    int result = 0;
    for (int j = 0; j < length; ++j)
    {
        if (s[(j + i) % s.length()] == 'b')
        {
            result++;
        }
    }
    return result;
}

int main()
{
    cin >> s;
    char first = s[0];
    char last = s[s.length() - 1];
    int i = 0;
    int j = s.length() - 1;
    int result = s.length();

    int a = 0;
    for (auto &ch : s)
    {
        if (ch == 'a')
        {
            a++;
        }
    }

    for (int i = 0; i < s.length(); ++i)
    {
        result = min(bCount(i, a), result);
    }

    cout << result;

    return 0;
}