#include <stdio.h>

int A, B, N, M;

struct Robot
{
    int x;
    int y;
    int c;
};

int grids[100][100] = {
    0,
};

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, -1, 0, 1};
Robot robots[101] = {};

int main()
{
    scanf("%d %d", &A, &B);
    scanf("%d %d", &N, &M);

    for (int i = 1; i <= N; ++i)
    {
        int x, y, intD;
        char d;
        scanf("%d %d %c", &x, &y, &d);

        if (d == 'N')
        {
            intD = 0;
        }
        else if (d == 'W')
        {
            intD = 1;
        }
        else if (d == 'S')
        {
            intD = 2;
        }
        else if (d == 'E')
        {
            intD = 3;
        }

        grids[x][y] = i;
        robots[i] = Robot{x, y, intD};
    }

    for (int i = 0; i < M; ++i)
    {
        int robotNumber;
        char command;
        int count;

        scanf("%d %c %d", &robotNumber, &command, &count);
        Robot robot = robots[robotNumber];
        int x = robot.x;
        int y = robot.y;
        int d = robot.c;
        if (command == 'F')
        {
            for (int j = 0; i < count; ++j)
            {
                grids[x][y] = 0;
                x += dx[d], y += dy[d];
                if (x < 1 || x > B || y < 1 || y > A)
                {
                    printf("Robot %d crashes into the wall", robotNumber);
                    for (j++; j < count; j++)
                    {
                        std::cin >> robotNumber >> command >> count;
                    }
                    return 0;
                }
                if (grids[x][y] != 0)
                {
                    int Y = grids[x][y];
                    printf("Robot %d crashes into robot %d", robotNumber, Y);
                    return 0;
                }
                grids[x][y] = robotNumber;
            }
        }
        else if (command == 'L')
        {
            d += 1, d %= 4;
        }
        else if (command == 'R')
        {
            d -= 1, d %= 4;
        }

        robots[robotNumber] = Robot{x, y, d};
    }
    printf("OK");

    return 0;
}