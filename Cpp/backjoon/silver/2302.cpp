#include <iostream>

using namespace std;

int main()
{
    int N;
    int M;
    int ns[41] = {
        1,
    };
    int result = 1;
    ns[1] = 1;
    int ms[41] = {};

    cin >> N >> M;

    for (int i = 0; i < M; ++i)
        cin >> ms[i];

    for (int i = 2; i <= N; ++i)
    {
        ns[i] = ns[i - 1] + ns[i - 2];
    }

    int before = 0;
    int after = 0;

    for (int m = 0; m < M; ++m)
    {
        after = ms[m];
        result *= ns[after - before - 1];
        // cout << result << ns[after - before - 1] << endl;
        before = after;
    }

    cout << result * ns[N - after];

    return 0;
}