#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
using namespace std;
int d[1001][1001];
void getInput(vector<int> &cards){
    int n;
    cin>>n;
    for(int i=0; i<n; i++){
        int card; cin>>card;
        cards.push_back(card);
    }
}
void flush(){
    for(int i =0; i< 1001; i++){
        memset(d[i],0,sizeof(d[i]));
    }
}
int dp(int head, int tail,vector<int> cards,int flag){
    if(d[head][tail]!=0){
        return d[head][tail];
    }
    if(head==tail){
        d[head][tail]=cards[head];
        return d[head][tail]; 
    }
        else {
        int pickLeft = dp(head+1,tail,cards,!flag);
        int pickRight = dp(head,tail-1,cards,!flag);
        if(pickRight>pickLeft){
            d[head][tail]=pickLeft-cards[head];
            return  d[head][tail];
        }
        else{ 
            d[head][tail]=pickLeft-cards[tail];
            return d[head][tail];
        }
    } 
}
int main(){
    int testCase;
    cin>>testCase;
    while(testCase--){
        vector<int> cards;
        getInput(cards);
        int test;
        test = dp(0,cards.size()-1, cards,1);
        cout<<"answer : "<<test<<endl;
        flush();
    }

    return 0;
}
