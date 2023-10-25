#include <stdio.h>

int N;
char state[100001];
char target[100001];
int result = -1;

void flip(char (&target)[100001], int n)
{
    if (n == -1 || n == N)
        return;
    if (target[n] == '1')
        target[n] = '0';
    else
        target[n] = '1';
}

void dfs(const int count, const int index)
{
    if (result != -1 && count >= result)
    {
        return;
    }
    if (index >= N)
    {
        if (state[N - 1] == target[N - 1] && state[N - 2] == target[N - 2])
        {
            result = count;
        }
        return;
    }

    if (index == 0)
    {
        dfs(count, index + 1);
        flip(state, index - 1);
        flip(state, index);
        flip(state, index + 1);
        dfs(count + 1, index + 1);
        flip(state, index - 1);
        flip(state, index);
        flip(state, index + 1);
        return;
    }
    if (target[index - 1] == state[index - 1])
    {
        dfs(count, index + 1);
    }
    else
    {
        flip(state, index - 1);
        flip(state, index);
        flip(state, index + 1);
        dfs(count + 1, index + 1);
        flip(state, index - 1);
        flip(state, index);
        flip(state, index + 1);
    }
}

int main()
{
    scanf("%d", &N);
    scanf("%s", &state);
    scanf("%s", &target);
    dfs(0, 0);
    printf("%d", result);
    return 0;
}