#include <iostream>
#include <algorithm>

using namespace std;
int N;
int arr[100001];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    // range 1, N + 1;
    for (int n = 1; n <= N; ++n)
    {
        cin >> arr[n];
    }

    // 1 2 3 4 5 12 23 34 45 123 234 345
    int start = 0;
    int visited[100001] = {};
    fill_n(visited, 0, 100001);
    long long result = 0;
    for (int n = 1; n <= N; ++n)
    {
        //        cout << result << "\n";
        if (visited[arr[n]] == 0)
        {
            result += n - start;
            visited[arr[n]] = n;
        }
        else
        {
            if (visited[arr[n]] > start)
            {
                start = visited[arr[n]];
            }
            result += n - start;
            visited[arr[n]] = n;
        }
    }
    cout << result;

    return 0;
}
