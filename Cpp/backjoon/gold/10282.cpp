#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int T;

int solve()
{
    int N, D, C;

    cin >> N >> D >> C;

    int a, b, s;
    priority_queue<pair<int, int>> pq;
    pq.push(make_pair(0, C));
    vector<pair<int, int>>
        grid[10001];
    while (D--)
    {
        cin >> a >> b >> s;
        grid[b].push_back(make_pair(a, s));
    }

    int dist[10001];
    fill_n(dist, 10001, -1);
    dist[C] = 0;

    // 다익스트라 시작

    while (!pq.empty())
    {
        int cost = -pq.top().first;
        int here = pq.top().second;
        pq.pop();

        for (int i = 0; i < grid[here].size(); ++i)
        {
            auto there = grid[here][i].first;
            auto newCost = grid[here][i].second + cost;

            if (dist[there] == -1 || dist[there] > newCost)
            {
                dist[there] = newCost;
                pq.push({-newCost, there});
            }
        }
    }

    int infestedCount = 0;
    int maxTime = 0;
    for (int i = 0; i < 10001; i++)
    {
        if (dist[i] != -1)
        {
            infestedCount++;
            maxTime = max(maxTime, dist[i]);
        }
    }

    cout << infestedCount << " " << maxTime << "\n";
    return 0;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> T;

    while (T--)
    {
        solve();
    }
    return 0;
}
