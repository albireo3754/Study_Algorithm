#include <stdio.h>
#include <algorithm>
#include <queue>

using namespace std;

int N, H, T;

int hit(int height)
{
    return height >= 2 ? height / 2 : 1;
}

int main()
{
    scanf("%d %d %d", &N, &H, &T);
    priority_queue<int> pq;

    for (int n = 0; n < N; ++n)
    {
        int d;
        scanf("%d", &d);
        pq.push(d);
    }

    int count = 0;
    int top = pq.top();
    while (T-- && top >= H)
    {
        pq.pop();
        pq.push(hit(top));
        count++;
        top = pq.top();
    }

    if (top >= H)
    {
        printf("NO\n%d", top);
    }
    else
    {
        printf("YES\n%d", count);
    }
    return 0;
}