#include <stdio.h>
#include <cstdlib>
#include <string>
#include <iostream>

using namespace std;

int N, M;
int grid[4][4];

// visited가 0이여야함
bool available(int i, int j, int visited)
{
    return !(visited & (1 << ((i)*M + j)));
}

void mask(int i, int j, int &bit)
{
    bit |= (1 << ((i)*M + j));
}

void unmask(int i, int j, int &bit)
{
    bit &= ~(1 << ((i)*M + j));
}

// 1일때 horizontal
bool isHorizontal(int i, int j, int bit)
{
    return (bit & (1 << ((i)*M + j)));
}

int result = 0;

int dfs(int i, int j, int sum, const int bit)
{

    int temp = 0;
    // 세로 or 제자리
    int visited = bit;
    if (i >= N || j >= M)
    {
        return 0;
    }
    for (int k = i; k < N && available(k, j, visited); ++k)
    {
        temp += grid[k][j];
        mask(k, j, visited);
        result = max(result, sum + temp);
        dfs((j + 1) / M + i, (j + 1) % M, sum + temp, visited);
        temp *= 10;
    }
    // 가로
    temp = grid[i][j] * 10;
    visited = bit;
    mask(i, j, visited);
    for (int k = j + 1; k < M && available(i, k, visited); ++k)
    {
        temp += grid[i][k];
        mask(i, k, visited);
        result = max(result, sum + temp);
        dfs((k + 1) / M + i, (k + 1) % M, sum + temp, visited);
        temp *= 10;
    }
    return temp;
}

void dp()
{
    for (int i = 0; i < 1 << (N * M); ++i)
    {
        //        cout << result << endl;

        //        if (i == 11) {
        //            cout << result;
        //        }
        int visited = 0;
        int sum = 0;
        for (int a = 0; a < N; ++a)
        {
            for (int b = 0; b < M; ++b)
            {
                int temp = 0;
                int n = a;
                int m = b;

                // 가로 평가
                while (n < N && m < M && available(n, m, visited) && isHorizontal(n, m, i))
                {
                    mask(n, m, visited);
                    temp *= 10;
                    temp += grid[n][m];
                    m++;
                }

                sum += temp;

                temp = 0;

                // 세로 평가
                while (n < N && m < M && available(n, m, visited) && !isHorizontal(n, m, i))
                {
                    mask(n, m, visited);
                    temp *= 10;
                    temp += grid[n][m];
                    n++;
                }

                sum += temp;
            }
        }

        result = max(sum, result);
    }
}

int main()
{
    scanf("%d %d", &N, &M);
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            scanf("%1d", &grid[i][j]);
        }
    }

    // dfs(0, 0, 0, 0);
    dp();

    printf("%d\n", result);

    return 0;
}
