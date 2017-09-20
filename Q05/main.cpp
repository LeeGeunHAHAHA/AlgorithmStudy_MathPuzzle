#include<cstdio>
#include<algorithm>
#include<iostream>
using namespace std;
int* x,* y;
pair<int, int> p[200000];
int main() {
    int testCase;
    cin>>testCase;
        while (testCase--){
             x = new int[100000]; y = new int[100000];
            int cnt, s, r, n ,d;
            cnt =0; s=0; r=0; n=0; d=0;
            scanf("%d", &n);
            for (int i = 0; i<n; i++) scanf("%d%d", x + i, y + i);
            scanf("%d", &d);
            for (int i = 0; i<n; i++) {
                if (x[i]>y[i]) swap(x[i], y[i]);
                if (y[i] - x[i]>d) continue;
                p[cnt++] = { y[i] - d,-1 };
                p[cnt++] = { x[i],1 };
            }
            sort(p, p + cnt);
            for (int i = 0; i<cnt; i++) {
                s -= p[i].second;
                if (r<s) r = s;
            }
            printf("%d", r);
            delete x, y;

    }
            return 0;
   }
