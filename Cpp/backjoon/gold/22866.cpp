#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int N;
int grid[100001];
pair<int, int> result[100001];
priority_queue<pair<int, int>> leftPq{};
priority_queue<pair<int, int>> rightPq{};
int main()
{
    cin >> N;
    // 문제의 1 <= i <= N
    for (int n = 1; n <= N; ++n)
    {
        cin >> grid[n];
        result[n] = make_pair(0, 0);
    }

    for (int i = 1; i <= N; ++i)
    {
        while (leftPq.empty() == false && grid[i] >= -leftPq.top().first)
        {
            leftPq.pop();
        }
        // 왼쪽 계산
        if (leftPq.empty() == false)
        {
            result[i].first = leftPq.size();
            result[i].second = leftPq.top().second;
        }
        leftPq.emplace(-grid[i], i);
    }

    for (int i = N; i >= 1; --i)
    {
        while (rightPq.empty() == false && grid[i] >= -rightPq.top().first)
        {
            rightPq.pop();
        }
        // 왼쪽 계산
        if (rightPq.empty() == false)
        {
            result[i].first += rightPq.size();
            if (result[i].second == 0 || i - result[i].second > rightPq.top().second - i)
            {
                result[i].second = rightPq.top().second;
            }
        }
        rightPq.emplace(-grid[i], i);
    }

    for (int i = 1; i <= N; ++i)
    {
        if (result[i].first == 0)
            cout << 0;
        else
            cout << result[i].first << ' ' << result[i].second;
        cout << '\n';
    }
    return 0;
}
