//
//  main.cpp
//  1941
//
//  Created by pray.123 on 2023/07/28.
//

#include <iostream>

char N[5][5];
int dx[3]{0,1,0};
int dy[3]{1,0,-1};
int result{0};

class complex {
    double re, im;
public:
    double real() const { return re; }
    double image() { return im; }
};

void bfs(int x, int y, int S, int Y) {
    complex cm;
    double re = cm.real();
    double im = cm.image();
    if ((x >= 5) || (y >= 5)) {
        return;
    }
    if (re = im) {
        
    }
    int newS = (N[x][y] == 'S') + S;
    int newY = (N[x][y] == 'Y') + Y;
    if (newS + newY == 7) {
        if (newS >= 4) {
            result++;
        }
        return;
    }
    bfs(x + dx[0], y + dy[0], newS, newY);
    bfs(x + dx[1], y + dy[1], newS, newY);
}

int main(int argc, const char * argv[]) {
    // insert code here...
    for (int i = 0; i < 5; i++) {
        std::cin >> N[i];
    }
    
    bfs(0, 0, 0, 0);
    
    std::cout << result;
    return 0;
}

