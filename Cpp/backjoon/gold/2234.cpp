#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int N, M;

int grid[51][51];
int visited[51][51];

int dx[4] = {0, -1, 0, 1};
int dy[4] = {-1, 0, 1, 0};
int areas[2501] = {};

queue<pair<int, int>> q = {};

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> M >> N;

    int temp = 0;
    for (int n = 0; n < N; ++n)
    {
        for (int m = 0; m < M; ++m)
        {
            cin >> temp;
            grid[n][m] = temp;
        }
    }

    int roomCount = 0;
    int maxArea = 0;
    for (int n = 0; n < N; ++n)
    {
        for (int m = 0; m < M; ++m)
        {
            // 방문한적이 있으면 0 이아님
            if (visited[n][m] != 0)
            {
                continue;
            }
            visited[n][m] = ++roomCount;
            q.push({n, m});
            int tempArea = 1;
            while (q.empty() == false)
            {
                auto [x, y] = q.front();
                q.pop();

                for (int d = 0; d < 4; ++d)
                {
                    int path = grid[x][y];
                    if ((path & (1 << d)))
                        continue;
                    int nx = x + dx[d], ny = y + dy[d];
                    if (nx < 0 || nx >= N || ny < 0 || ny >= M || visited[nx][ny] != 0)
                        continue;

                    visited[nx][ny] = roomCount;
                    q.push({nx, ny});
                    tempArea++;
                }
            }
            areas[roomCount] = tempArea;
            maxArea = max(maxArea, tempArea);
        }
    }

    int breakWall = 0;
    // 3번 계산하기
    for (int n = 0; n < N; ++n)
    {
        for (int m = 0; m < M; ++m)
        {
            // 방문한적이 있으면 0 이아님
            for (int d = 0; d < 4; ++d)
            {
                int path = grid[n][m];
                // 위와 반대로 벽이 없으면 무시
                if ((path & (1 << d)) == 0)
                    continue;
                int nx = n + dx[d], ny = m + dy[d];
                if (nx < 0 || nx >= N || ny < 0 || ny >= M || visited[nx][ny] == visited[n][m])
                    continue;

                breakWall = max(breakWall, areas[visited[nx][ny]] + areas[visited[n][m]]);
            }
        }
    }

    //    for (int i = 0; i < N; ++i) {
    //        for (int j = 0; j < M; ++j) {
    //            cout << visited[i][j];
    //        }
    //        cout << "\n";
    //    }
    //    for (int i = 0; i < N; ++i) {
    //        cout << areas[i];
    //    }

    cout << roomCount << "\n"
         << maxArea << "\n"
         << breakWall;
}
