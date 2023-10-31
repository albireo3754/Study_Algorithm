#include <stdio.h>
#include <string>
#include <iostream>
#include <set>

using namespace std;

int result = 0;

int dp(string target, int base)
{
    set<pair<string, int>> s{};

    for (int i = 0; i < target.length() - 1; ++i)
    {
        set<pair<string, int>> temp{};
        string ch = string{target.at(i)};

        if (stoi(ch) < base)
        {
            int chCount = 0;
            for (auto p : s)
            {
                chCount += p.second;
            }
            temp.insert(make_pair(ch, chCount));
        }

        for (auto p : s)
        {
            p.first.append(ch);
            if (stoi(p.first) < base)
            {
                temp.insert(p);
            }
        }

        s = temp;
    }

    for (auto p : s)
    {
        chCount += result;
    }
}

int main()
{
    string s;
    cin >> s;

    for (int base_i = s.length() - 1; base_i > 0; --base_i)
    {
        if (s.at(base_i) == '0')
        {
            continue;
        }
        dp(s.substr(0, base_i), stoi(s.substr(base_i)));
    }
    return 0;
}