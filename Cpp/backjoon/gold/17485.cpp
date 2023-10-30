#include <stdio.h>
#include <iostream>
#include <algorithm>

int N, M;
int grid[1001][1001][4] = {
    0,
};
int dy[4] = {0, -1, 0, 1};
int result = 100 * 1000 + 1;

void dp()
{
    for (int x = 2; x <= N; ++x)
    {
        for (int y = 1; y <= M; ++y)
        {
            for (int dir = 1; dir <= 3; ++dir)
            {
                int dy = y + 2 - dir;
                if (dy == 0 || dy == M + 1)
                {
                    grid[x][y][dir] = 100 * 1000 + 1;
                }
                else
                {
                    // dir 1 왼쪽
                    // dir 2 직진
                    // dir 3 오른쪽
                    grid[x][y][dir] = grid[x][y][0] + std::min(grid[x - 1][y + (2 - dir)][dir + 1 <= 3 ? dir + 1 : (dir + 1) % 3], grid[x - 1][y + (2 - dir)][dir + 2 <= 3 ? dir + 2 : (dir + 2) % 3]);
                }
                // printf("%d %d %d %d \n", x, y, dir, grid[x][y][dir]);
                if (x == N)
                {
                    result = std::min(grid[x][y][dir], result);
                }
            }
        }
    }
}

int main()
{
    scanf("%d %d", &N, &M);
    for (int i = 1; i <= N; ++i)
    {
        for (int m = 1; m <= M; ++m)
            std::cin >> grid[i][m][0];
    }

    for (int m = 1; m <= M; ++m)
    {
        for (int dir = 1; dir <= 3; ++dir)
        {
            grid[1][m][dir] = grid[1][m][0];
        }
    }

    dp();
    printf("%d", result);

    return 0;
}