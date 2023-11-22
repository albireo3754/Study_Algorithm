#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int N, L, R;

int grid[52][52]{};
int unions[52][52]{};

int dx[4]{0, 1, 0, -1};
int dy[4]{1, 0, -1, 0};
int visited[52][52]{};

bool canUnion(int x, int y)
{
    int big = x >= y ? x : y;
    int small = x >= y ? y : x;
    int diff = big - small;
    return diff >= L && diff <= R;
}

struct UnionTask
{
    int x;
    int y;
    int ally;

    UnionTask(int x, int y, int ally) : x(x), y(y), ally(ally){};
};

pair<int, int> bfs(int i, int j, int ally, bool *isUnion)
{
    queue<UnionTask> q = {};

    q.emplace(i, j, ally);

    visited[i][j] = ally;

    int total = grid[i][j];
    int count = 1;
    while (q.empty() == false)
    {
        auto [x, y, ally] = q.front();
        q.pop();

        for (int dd = 0; dd < 4; ++dd)
        {
            int nx = x + dx[dd];
            int ny = y + dy[dd];

            if (nx < 1 || nx > N || ny < 1 || ny > N || visited[nx][ny])
            {
                continue;
            }
            if (canUnion(grid[x][y], grid[nx][ny]))
            {
                *isUnion = true;
                visited[nx][ny] = ally;
                q.emplace(nx, ny, ally);
                total += grid[nx][ny];
                count += 1;
            }
        }
    }
    return make_pair(total, count);
}

bool _union()
{
    vector<pair<int, int>> allys = {};

    bool isUnion = false;
    for (int i = 1; i <= N; ++i)
    {
        for (int j = 1; j <= N; ++j)
        {
            if (visited[i][j] == 0)
            {
                auto [total, count] = bfs(i, j, allys.size() + 1, &isUnion);
                allys.emplace_back(total, count);
            }
        }
    }

    if (!isUnion)
    {
        return false;
    }

    for (int i = 1; i <= N; ++i)
    {
        for (int j = 1; j <= N; ++j)
        {
            auto ally = allys[visited[i][j] - 1];
            if (ally.second == 1)
            {
                continue;
            }
            grid[i][j] = ally.first / ally.second;
        }
    }

    // for (int i = 1; i <= N; ++i)
    // {
    //     for (int j = 1; j <= N; ++j)
    //     {
    //         cout << visited[i][j] << " ";
    //     }
    //     cout << "\n";
    // }

    return true;
}

int sim()
{
    int result = 0;
    while (_union())
    {
        memset(visited, 0, sizeof(visited));
        result++;
    }
    return result;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> L >> R;

    for (int n = 1; n <= N; ++n)
    {
        for (int j = 1; j <= N; ++j)
        {
            cin >> grid[n][j];
        }
    }

    cout << sim();

    return 0;
}
