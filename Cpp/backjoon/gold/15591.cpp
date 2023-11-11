#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;
int N, Q;

int grid[5001][5001]{};
vector<pair<int, int>> grid2[5001];

void dijk(int k, int start)
{
    int minUsados[5001]{};
    fill_n(minUsados, 5001, -1);
    priority_queue<pair<int, int>> pq = {};
    minUsados[start] = 0;
    pq.push(make_pair(0, 3));

    while (!pq.empty())
    {
        auto [weight, here] = pq.top();
        pq.pop();
        weight = weight * -1;

        for (auto [usado, there] : grid2[here])
        {
            int newUsado = min(usado, weight);
            if (minUsados[there] == -1 && minUsados[there] > newUsado)
            {
                minUsados[there] = newUsado;
                pq.push(make_pair(-newUsado, there));
            }
        }
    }
}

int bfs(int k, int start)
{
    int visited[5001]{};

    queue<pair<int, int>> q{};
    q.emplace(start, 0);

    while (q.empty() == false)
    {
        int here = q.front().first;
        int usado = q.front().second;
        q.pop();

        for (auto p : grid2[here])
        {
            int newUsado = max(usado, p.second);
            if (visited[p.first] == 0 || visited[p.first] < newUsado)
            {
                visited[p.first] = newUsado;
                q.emplace(p.first, newUsado);
            }
        }
    }
    int count = 0;
    for (int i = 0; i <= 5000; ++i)
    {
        if (visited[i] >= k)
        {
            count++;
        }
    }
    cout << count;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> Q;
    int p, q, r;
    for (int n = 0; n < N - 1; ++n)
    {
        cin >> p >> q >> r;
        grid2[p].push_back(make_pair(q, r));
        grid2[q].push_back(make_pair(p, r));
    }

    int k, v;
    for (int q = 0; q < Q; ++q)
    {
        // 1 <= k <= 10억 (int)
        // 1 <= v <= N(pair) usado가 k이상일때 v를 보고있는 소 추천수
        cin >> k >> v;
        // dijk(k, v);
        bfs(k, v);
    }

    return 0;
}