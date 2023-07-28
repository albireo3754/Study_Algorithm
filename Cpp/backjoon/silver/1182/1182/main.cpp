//
//  main.cpp
//  1182
//
//  Created by pray.123 on 2023/07/28.
//

#include <iostream>
#include <algorithm>

int N, S;
int arr[30] = {0};
int result[50000001] = {0};

void search(int n, int temp) {
    if (n == N) {
        return;
    }
    search(n + 1, temp);
    temp += arr[n];
    result[temp + 25000000] += 1;
    search(n + 1, temp);
}

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cin >> N >> S;
    
    for (int i = 0; i < N; i++) {
        std::cin >> arr[i];
    }
    std::sort(arr, arr + N);
    
    search(0, 0);
    
    std::cout << result[S + 25000000];

    return 0;
}

