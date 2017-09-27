#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
bool func(int i, int j){
    int a = i; int b = j;
    if(a<0)a*=-1;
    if(b<0)b*=-1;
    return a<b;
}
int main(){
    int testCase;
    cin>>testCase;
    while(testCase--){
    int n, k;
    cin>>n>>k;
    int * arr = new int[n];
    vector<int> sums;
    for(int i =0; i<n ; i++){
        int tmp;
        cin>>tmp;
        arr[i] =tmp;
    }
    for(int i =0; i<n; i++){
        for(int j =i+1; j<n; j++){
            sums.push_back((arr[i]+arr[j]-k)<0?-(arr[i]+arr[j]-k):(arr[i]+arr[j]-k));            

        }
    }
    //sort(sums.begin(),sums.end(),func);
    sort(sums.begin(),sums.end());
    int cnt =1;
    for(int i=0; i<sums.size(); i++){
    if(sums[i]==sums[i+1] || sums [i]==-sums[i+1]) cnt+=1;
    else break;
    }
    cout<<cnt<<endl;
    delete arr;
    }
     return 0;
}
