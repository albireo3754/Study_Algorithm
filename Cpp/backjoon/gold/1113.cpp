#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int N, M;
int grid[52][52];

int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
int visited[52][52];

int bfs(int i, int j)
{
    if (grid[i][j] > grid[i - 1][j])
    {
        visited[i][j] = 1;
        return 0;
    }
    int height = grid[i - 1][j] - grid[i][j];
    queue<pair<int, int>> q = {};
    priority_queue<pair<int, int>> pq = {};
    q.push(make_pair(i, j));
    int maxHeight = 10;
    int minHeight = grid[i][j];

    while (q.empty() == false)
    {
        auto [x, y] = q.front();
        q.pop();
        for (int dd = 0; dd < 4; ++dd)
        {
        
            int nx = x + dx[dd];
            int ny = y + dy[dd];
            if (grid[nx][ny] == 0) {
                return 0;
            }
            maxHeight = max(maxHeight, grid[nx][ny]);
            minHeight = min(minHeight, grid[nx][ny]);
            if (visited[nx][ny]) {
                continue;
            }
            visited[nx][ny] = 1;
            q.emplace(nx, ny);
        }
    }

    // 물이 넘치면 항상
    return 0;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M;

    // 0 ~ 50 * 50 * 9;
    int result = 0;

    for (int n = 1; n <= N; ++n)
    {
        for (int m = 1; m <= M; ++m)
        {
            cin >> grid[n][m];
        }
    }
}