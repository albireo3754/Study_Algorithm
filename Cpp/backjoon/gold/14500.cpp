#include <iostream>

using namespace std;

int N, M;
int grids[501][501];
int visited[501][501] = {};
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
int result = 0;

void solve2(int n, int m)
{
    int temp = grids[n][m];
    bool flag = false;
    for (int dd = 0; dd < 4; ++dd)
    {
        int nx = n + dx[dd];
        int ny = m + dy[dd];
        if (0 > nx || nx >= N || ny < 0 || ny >= M)
        {
            if (flag == false)
            {
                flag = true;
            }
            else
            {
                return;
            }
        }
        else
        {
            temp += grids[nx][ny];
        }
    }

    if (flag)
    {
        result = max(result, temp);
    }
    else
    {
        for (int dd = 0; dd < 4; ++dd)
        {
            int nx = n + dx[dd];
            int ny = m + dy[dd];
            result = max(result, temp - grids[nx][ny]);
        }
    }
}
void solve(int n, int m, int d, int temp)
{
    temp += grids[n][m];
    if (d == 3)
    {
        result = max(result, temp);
        return;
    }

    for (int dd = 0; dd < 4; ++dd)
    {
        int nx = n + dx[dd];
        int ny = m + dy[dd];
        if (0 > nx || nx >= N || ny < 0 || ny >= M || visited[nx][ny])
        {
            continue;
        }

        visited[nx][ny] = true;
        solve(nx, ny, d + 1, temp);
        visited[nx][ny] = false;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M;
    for (int n = 0; n < N; ++n)
    {
        for (int m = 0; m < M; ++m)
        {

            cin >> grids[n][m];
        }
    }

    for (int n = 0; n < N; ++n)
    {
        for (int m = 0; m < M; ++m)
        {
            if (n == 2 && m == 2)
            {
                int x = 5;
            }
            // visited[n][m] = true;
            solve(n, m, 0, 0);
            solve2(n, m);
        }
    }

    cout << result;

    return 0;
}