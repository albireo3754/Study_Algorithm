#include <iostream>

using namespace std;

// N TabMax;
int N, K;
// K의 배열
int tabs[101];
int arrs[101];
bool isPlugin[101]{};
int result = 0;
int currentTab = 0;

void greedy()
{
    // K == 7
    for (int order = 0; order < K; ++order) {

    if (isPlugin[arrs[order]])
    {
        continue;
    }
    
    if (currentTab == N)
    {
        int last = -1;
        int plugOutTarget = 0;
        for (int n = 0; n < N; ++n) {
            int temp = K + 1;
            for (int i = order + 1; i < K; ++i)
            {
                if (arrs[i] == tabs[n])
                {
                    temp = i;
                    break;
                }
            }
            if (temp > last)
            {
                plugOutTarget = n;
                last = temp;
            }
        }
        int dry = tabs[plugOutTarget];
        isPlugin[dry] = false;
        isPlugin[arrs[order]] = true;
        tabs[plugOutTarget] = arrs[order];
        result++;
    }
    else
    {
        tabs[currentTab] = arrs[order];
        isPlugin[arrs[order]] = true;
        currentTab++;
    }
    }
}
void dfs(int order, int plugOutCount)
{
    if (plugOutCount >= result)
    {
        return;
    }
    // K == 7
    if (order == K)
    {
        result = plugOutCount;
        return;
    }

    if (isPlugin[arrs[order]])
    {
        return dfs(order + 1, plugOutCount);
    }
    
    if (currentTab == N)
    {
        for (int n = 0; n < N; ++n) {
            int current = tabs[n];
            isPlugin[current] = false;
            isPlugin[arrs[order]] = true;
            dfs(order + 1, plugOutCount + 1);
            isPlugin[arrs[order]] = false;
            isPlugin[current] = true;
        }
    }
    else
    {
        tabs[currentTab] = arrs[order];
        isPlugin[arrs[order]] = true;
        currentTab++;
        dfs(order + 1, plugOutCount);
    }
}

void bf()
{
    //하나씩 꼽고 다차면 순서대로 돌면서 하나씩 뽑아본다.

}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> K;
    for (int k = 0; k < K; ++k)
    {
        cin >> arrs[k];
    }

    // brtue
    greedy();

    cout << result;

    return 0;
}
