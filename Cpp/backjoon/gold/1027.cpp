#include <iostream>
#include <algorithm>
using namespace std;

int N;
int builds[51];

int solve(int i)
{
    // left 1 ~ i - 1
    // right i + 1 ~ N

    int diff = 0;
    int diffIndex = 0;
    int result = 0;
    if (i > 1)
    {
        diff = builds[i] - builds[i - 1];
        diffIndex = i - 1;
        result++;
        for (int j = i - 2; j > 0; --j)
        {
            if ((double)diff / (double)(i - diffIndex) * (double)(i - j) > (double)(builds[i] - builds[j]))
            {
                diff = builds[i] - builds[j];
                diffIndex = j;
                result++;
            }
        }
    }

    if (i < N)
    {
        diff = builds[i] - builds[i + 1];
        diffIndex = i + 1;
        result++;
        for (int j = i + 2; j <= N; ++j)
        {
            if ((double)diff / (double)(i - diffIndex) * (double)(i - j) > (double)(builds[i] - builds[j]))
            {
                diff = builds[i] - builds[j];
                diffIndex = j;
                result++;
            }
        }
    }
    return result;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;

    for (int i = 1; i <= N; ++i)
    {
        cin >> builds[i];
    }

    int result = 0;
    for (int i = 1; i <= N; ++i)
    {
        result = max(solve(i), result);
    }
    cout << result;

    return 0;
}