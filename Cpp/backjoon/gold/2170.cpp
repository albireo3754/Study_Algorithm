#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int N;
    int result = 0;
    std::cin >> N;
    std::vector<std::pair<int, int>> v;
    for (int i = 0; i < N; ++i)
    {
        int x, y;
        scanf("%d %d", &x, &y);
        v.push_back(std::make_pair(x, y));
    }

    std::sort(v.begin(), v.end(), [](const std::pair<int, int> &left, const std::pair<int, int> &right)
              { return left.first < right.first; });

    int first, second = -1000000001;

    for (const std::pair<int, int> p : v)
    {
        if (second <= p.first)
        {
            result += second - first;
            first = p.first;
            second = p.second;
            continue;
        }

        if (second <= p.second)
        {
            continue;
        }

        second = p.second;
    }

    std::cout << result + (p.second - p.first) << std::endl;
    return 0;
}