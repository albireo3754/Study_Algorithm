#include <stdio.h>
#include <string>
#include <iostream>
<<<<<<< HEAD
=======
#include <vector>
#include <algorithm>
>>>>>>> d18aa3b (풀이를 알 수 없음)
#include <set>

using namespace std;

<<<<<<< HEAD
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
=======
set<vector<string>> memo = {};
>>>>>>> d18aa3b (풀이를 알 수 없음)

int main()
{
    string s;
    cin >> s;
    int result = 0;

<<<<<<< HEAD
    for (int base_i = s.length() - 1; base_i > 0; --base_i)
    {
        if (s.at(base_i) == '0')
        {
            continue;
        }
        dp(s.substr(0, base_i), stoi(s.substr(base_i)));
=======
    if (s.at(0) == '0') {
        cin >> result;
        return 0;
>>>>>>> d18aa3b (풀이를 알 수 없음)
    }
    char target = s.at(0);
    string iter = s.substr(1);

    for (int i = 1; i < s.length(); ++i) {
        string new_s { s.at(i) };
        while (i < s.length() - 1 && s.at(i + 1) != '0') {
            new_s.push_back(++i);
        }
        if (i == s.length() - 1) {
            break;
        }
        int base = stoi(s.substr(i));
        int temp = stoi(new_s);
        if (memo.size() == 0) {
            if (temp < base) {
                memo.insert({ new_s });    
                result+= 1;
            }
        } else {
            set<vector<string>> tempSet = {};
            for (auto m: memo) {
                for (auto _m: m) {
                    if (stoi(_m) < base) {
                        break;
                    }
                }
                vector<string> newVector;
                if (not break) {
                    copy(m.begin(), m.end(), newVector);
                }
            }
        }
    }

    // for (int base_i = s.length() - 1; base_i > 0; --base_i)
    // {

    // }
    cin >> result;
    return 0;
}