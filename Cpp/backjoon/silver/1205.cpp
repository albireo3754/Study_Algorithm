#include <iostream>

using namespace std;
// 0<= N <= P <= 50
// P는 arr의 MaxSize
int N, TESU, P;
// 정수는 0<= intMax
// 내림차순 정렬

int arr[55] = {};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    fill_n(arr, 55, -1);
    cin >> N >> TESU >> P;

    int rank = 1;
    int sameRank = 0;
    for (int n = 0; n < N; ++n)
    {
        cin >> arr[n];
        if (TESU < arr[n])
        {
            rank++;
        }
        else if (arr[n] == TESU)
        {
            sameRank++;
        }
        else
        {
            break;
        }
    }
    // cout << rank << sameRank;

    if (rank + sameRank <= P)
    {
        cout << rank;
    }
    else
    {
        cout << -1;
    }
}
