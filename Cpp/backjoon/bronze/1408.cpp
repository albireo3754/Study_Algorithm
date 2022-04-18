#include <stdio.h>
#include <assert.h>

int main() {
    int hh, mm, ss;
    int h, m, s;
    scanf("%d:%d:%d", &hh, &mm, &ss);
    scanf("%d:%d:%d", &h, &m, &s);
    int hhh, mmm, sss;
    int time = (h * 3600 - hh * 3600 + m * 60 - mm * 60 + s - ss) > 0 ? (h * 3600 - hh * 3600 + m * 60 - mm * 60 + s - ss): (h * 3600 - hh * 3600 + m * 60 - mm * 60 + s - ss) + 86400;
    hhh = time / 3600;
    mmm = (time % 3600) / 60;
    sss = time % 60;
    printf("%0*d:", 2, hhh);
    printf("%0*d:", 2, mmm);
    printf("%0*d", 2, sss);
    return 0;
}