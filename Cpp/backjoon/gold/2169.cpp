// N * M
// 왼, 오, 아
// 왼쪽위 1,1
// 탐사 가치 합 최대
// 가치는 range(-100, 101)
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

struct Search
{
    int x;
    int y;
    int weight;
    int dir;

    Search(int x, int y, int weight, int dir) : x(x),
                                                y(y),
                                                weight(weight),
                                                dir(dir)
    {
    }
};

int dx[3] = {0, 0, 1};
int dy[3] = {-1, 1, 0};
// bfs로 풀면되는데 visited를 어떻게 체크할까?
// 1 2 3   125 12365
// 4 5 6
int grid[1001][1001];
int N, M;
int dp[1001][1001][3];
bool visited[1001][1001];

int unvisited = -200000000;
int dfs(int x, int y, int dir)
{
    // cout << x << "," << y << "\n";
    if (x == N && y == M)
        return grid[N][M];

    if (dp[x][y][dir] != unvisited)
        return dp[x][y][dir];

    visited[x][y] = true;

    for (int dd = 0; dd < 3; ++dd)
    {
        int nx = x + dx[dd];
        int ny = y + dy[dd];

        // cout << nx << "," << ny << "\n";
        if (nx < 1 || nx > N || ny < 1 || ny > M || visited[nx][ny])
            continue;
        dp[x][y][dir] = max(dp[x][y][dir], dfs(nx, ny, dd) + grid[x][y]);
    }

    visited[x][y] = false;
    return dp[x][y][dir];
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M;
    for (int n = 1; n <= N; ++n)
        for (int m = 1; m <= M; ++m)
        {
            cin >> grid[n][m];
            dp[n][m][0] = unvisited;
            dp[n][m][1] = unvisited;
            dp[n][m][2] = unvisited;
        }

    cout << dfs(1, 1, 0);

    // for (int n = 1; n <= N; ++n)
    // {
    //     for (int m = 1; m <= M; ++m)
    //     {

    //         cout << dp[n][m][2] << ",";
    //     }

    //     cout << "\n";
    // }
    return 0;
}