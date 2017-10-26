#include <iostream>

using namespace std;

int d[101][11];
void process(){
    for(int i =0; i<11; i ++){
        d[1][i]=1;
    }
    d[1][0]=0;
    d[1][10]=0;
    for (int i =2; i<101; i++){
        for (int j =0; j<11; j++){
           if(j==10){
               d[i][j]=0;
           }
           else if (j ==0){ 
               d[i][j] = d[i-1][1];
           }
           else{ 
               d[i][j] = d[i-1][j-1]+d[i-1][j+1];
           } 
        }
    }
}

int main () {
    int n ;
    cin>>n;
    int sum =0;
    process();
    for (int i =0; i< 11; i++)
    {
     sum+=d[n][i];
    }
    cout<<sum%10000000000<<endl;
    
    return 0;
}
