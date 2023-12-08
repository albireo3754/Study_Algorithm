#include <iostream>
#include <queue>
#include <deque>
#include <algorithm>
using namespace std;

int N, K;

deque<pair<int, bool>> container = {};
int cnt = 0;
int start = 0;
int temp = 0;

int main()
{
    cin >> N >> K;
    int temp;
    for (int i = 0; i < 2 * N; ++i)
    {
        cin >> temp;
        container.emplace_back(temp, false);
    }

    int k = 0;
    temp = 0;

    while (true)
    {
        cnt++;
        // 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
        container.push_front(container.back());
        container.pop_back();

        if (container[N - 1].second == true)
        {
            container[N - 1] = make_pair(container[N - 1].first, false);
        }

        // 2.
        for (int i = N - 2; i >= 0; --i)
        {
            if (container[i].second == true && container[i + 1].first >= 1 && container[i + 1].second == false)
            {
                container[i + 1].second = true;
                container[i + 1].first -= 1;
                container[i].second = false;
                if (i + 1 == N - 1)
                {
                    container[i + 1].second = false;
                }

                if (container[i + 1].first == 0)
                {
                    temp++;
                }

                container[i + 1].second = true;
            }
        }

        // 3.
        if (container[0].first >= 1)
        {
            container[0].second = true;
            container[0].first -= 1;
            if (container[0].second)
            {
                temp++;
            }
        }

        if (temp >= K)
        {
            cout << cnt;
            return 0;
        }
    }

    return 0;
}