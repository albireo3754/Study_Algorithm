#include <stdio.h>
#include <iostream>
#include <cmath>

int N, K;
int arr[9];
int result = 0;
const int TARGET = 500;

void dfs(const int weight, const int used)
{
    // printf("%d, %d \n", weight, used);
    if (weight < 500)
    {
        return;
    }
    if (used == (1 << N) - 1)
    {
        result++;
        return;
    }

    for (int i = 0; i < N; ++i)
    {
        if (!(used & (1 << i)))
        {
            dfs(weight + arr[i] - K, used | (1 << i));
        }
    }
}

int main()
{
    scanf("%d %d", &N, &K);
    for (int i = 0; i < N; ++i)
    {
        scanf("%d", &arr[i]);
    }

    dfs(500, 0);
    // printf("%d \n", (1 << N) - 1);
    printf("%d", result);
}