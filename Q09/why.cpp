#include <iostream>
#include <cstdlib>
#include <cstring> 
#include <algorithm>
#include <vector> 
#include <deque> 
using namespace std;
vector<int> a;  
int dp[1001][1001][2];  
int solve(int l,int r,int turn){
    if (l > r) return 0;  
    int &ret = dp[l][r][turn];  
    if (ret != -1) return ret;  
    ret = 0;  
    if (turn == 1){ 
        ret = min(solve(l+1,r,0),solve(l,r-1,0));  
    }else{ 
        ret = max(a[l]+solve(l+1,r,1),a[r]+solve(l,r-1,1));  
    }
    return ret;  
}  
int main(){
    cin.tie(0); cout.tie(0);  
    int t; 
    cin >> t; 
    while (t--){
        a.clear();  
        memset(dp,-1,sizeof(dp));  
        int n;  
        cin >> n;  
        for (int i = 0; i < n; i++){
            int no; 
            cin >> no; 
            a.push_back(no); 
        }
        int ans = solve(0,n-1,0); 
        cout << ans << endl;   
    }
    return 0;  
}

