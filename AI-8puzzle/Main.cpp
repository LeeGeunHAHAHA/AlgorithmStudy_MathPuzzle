#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <list>
#include <deque>
#include <bits/stdc++.h>

#define mt(a,b,c) make_pair((a),(make_pair((b),(c))))
using namespace std;
vector< pair<int, int> > openQ;
vector< pair<int, int> > closedQ;
struct sort_second{
    bool operator()(const std::pair<int,int> &left, const std::pair<int, int> &right){
        return left.second< right.second;
    }
};
int calDist(int target){
    int start = 123804765;

    int dist = 0;
    while(target>0){
        if(target%10 != start%10&& target%10 !=0) dist ++;
        target/=10;
        start/=10;
    }

    return dist;

}

const int INF = 987654321;

int dx[] = {0,1,0,-1};
int dy[] = {-1,0,1,0};

int shift[11];
map<int,int> dist;
void printState(int state){
    for( int i =0; i< openQ.size(); i++){
    cout<<"in openQ : " << openQ[i].first<<",  h(n) : "<<openQ[i].second <<endl;
    }
    for( int i =0; i< closedQ.size(); i++){
    cout<<"in closedQ : " << closedQ[i].first<<",  h(n) : "<<closedQ[i].second <<endl;
    }
}

int bfs(int start)
{
    if(start == 123804765) return 0;

    dist[start] = 1;
    pair <int, int> st(start,calDist(start)); 
    openQ.push_back(st);

    while(!openQ.empty()){
        int cur =openQ.front().first;
        printState(cur);
        pair <int, int> close = openQ.front();
        closedQ.push_back(close);
        cout<<"-------------------------------------"<<endl;
        cout<<"current node  :   "<<cur<<endl;
        openQ.erase(openQ.begin());
        if (cur ==123804765) break;
        int one = 0;
        int d = dist[cur];
        int tmp = cur;
        for(int i=8;i>=0;--i){
            if(tmp%10==0){
                one = i;
                break;
            }
            tmp /= 10;
        }
        int x = one / 3;
        int y = one % 3;
        for(int i=0;i<4;++i){
            int X = x + dx[i];
            int Y = y + dy[i];
            if(X<0 || X>=3 || Y<0 || Y>=3)continue;
            int np = X*3 + Y;
            int od = ((cur/shift[np])%10)*shift[one];
            int nd = ((cur/shift[np])%10)*shift[np];
            int next = cur - nd + od;
            if(!dist[next]){
                pair<int,int> tmp(next,calDist(next)+d);
                openQ.push_back(tmp);
                dist[next] = d + 1;
                sort(openQ.begin(),openQ.end(),sort_second()); 
                
            }
        }

    }
    return dist[123804765] - 1;
}
int main()
{
    shift[0] = 1;
    for(int i=1;i<=10;++i)shift[i] = shift[i-1] * 10;
    for(int i=8;i>=4;--i){
        swap(shift[i],shift[8-i]);
    }
    int start = 0;
    for(int i=0;i<9;++i){
        int x;
        scanf("%d",&x);
        start *= 10;
        start += x;
    }
    printf("%d",bfs(start));
}
