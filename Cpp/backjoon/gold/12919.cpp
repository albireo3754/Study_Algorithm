#include <iostream>
#include <string>

using namespace std;

bool solve(string s, string t)
{
    // cout << s << " : " << t << "\n";
    if (s == t)
    {
        cout << 1;
        exit(0);
        return true;
    }
    if (s.length() >= t.length())
    {
        return false;
    }
    bool result = false;
    if (t[0] == 'B')
    {
        string temp = t;
        reverse(temp.begin(), temp.end());
        temp.pop_back();
        result |= solve(s, temp);
    }
    if (t[t.length() - 1] == 'A')
    {
        t.pop_back();
        result |= solve(s, t);
    }
    return result;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    string s, t;
    cin >> s >> t;
    solve(s, t);
    cout << 0;
}
