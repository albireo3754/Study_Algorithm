#include <iostream>
#include <vector>
#include <cstdint>
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;

    vector<vector<int>> fuel_cost_map(N, vector<int>(M));

    // dp_map[i][j]
    // first: (i, j) 까지 도달하는데 필요한 최소 비용
    // second: 이전 위치에서 움직인 방향, -1: 왼쪽 아래, 0: 아래, 1: 오른쪽 아래
    vector<vector<pair<int, int>>> dp_map(N, vector<pair<int, int>>(M, pair<int, int>(0, 0))); 
    

    for(int n = 0; n < N; n++)
        for(int m = 0; m < M; m++)
            cin >> fuel_cost_map[n][m];

    for(int m = 0; m < M; m++)
    {
        dp_map[0][m].first = fuel_cost_map[0][m];
        dp_map[0][m].second = 0;
    }

    for(int n = 0; n < N-1; n++)
        for(int m = 0; m < M; m++)
        {
            for(int dir:{-1, 0, 1})
            {
                if(dir == dp_map[n][m].second) continue;
                if(m+dir < 0) continue;
                if(m+dir >= M) continue;

                int cost = dp_map[n][m].first + fuel_cost_map[n+1][m+dir];
    
                if(dp_map[n+1][m+dir].first == 0 || dp_map[n+1][m+dir].first > cost)
                {
                    dp_map[n+1][m+dir].first = cost;
                    dp_map[n+1][m+dir].second = dir;
                }
            }
        }
    
    int min_fuel_cost = dp_map[N-1][0].first;
    for(int m = 1; m < M ; m++)
        min_fuel_cost = min(min_fuel_cost, dp_map[N-1][m].first);
    
    cout << min_fuel_cost;

    return 0;
}