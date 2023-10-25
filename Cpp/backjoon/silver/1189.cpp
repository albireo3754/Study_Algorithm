#include <iostream>
#include <stdio.h>
#include <string>

int dirrection[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
char arr[6][6];
int R, C, K;
int result = 0;
int start[2];
int end[2];

void dfs(int curr[2], int distance)
{
    int x = curr[0];
    int y = curr[1];
    arr[x][y] = 'T';
    // printf("%d %d \n", x, y);
    for (auto [dx, dy] : dirrection)
    {
        int nx = x + dx;
        int ny = y + dy;
        if (nx >= 0 && nx < R)
        {
            if (ny >= 0 && ny < C)
            {
                if (arr[nx][ny] == 'T')
                {
                    continue;
                }
                if (nx == end[0] && ny == end[1])
                {
                    // printf("distance: %d \n", distance);
                    if (distance == K - 1)
                    {
                        result++;
                    }
                    continue;
                }
                int newcurr[2] = {nx, ny};
                dfs(newcurr, distance + 1);
            }
        }
    }
    arr[x][y] = '.';
}
int main()
{
    scanf("%d %d %d", &R, &C, &K);
    for (int i = 0; i < R; i++)
    {
        scanf("%s", arr[i]);
    }
    start[0] = R - 1;
    start[1] = 0;
    end[0] = 0;
    end[1] = C - 1;

    dfs(start, 1);
    printf("%d", result);
}