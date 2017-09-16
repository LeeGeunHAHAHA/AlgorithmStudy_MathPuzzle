#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
vector<pair <int ,int> > data;
bool ordReverse(pair<int, int> a, pair<int,int> b){
    return a.second>b.second;
}
void makeReverse(int begin, int end){
    sort(data.begin()+begin, data.begin()+end,ordReverse);
}


void getInputSort(int n){
    int x,y;
    for(int i =0; i<n ; i++){
        cin>>x>>y;
        data.push_back(pair<int , int>(x,y));
    }
    sort(data.begin(),data.end());
    int end=0;
    for(int i =0; i<data.size(); i++){
        if(data[0].second!=0){
            if(data[i].first!=0||i==data.size()-1){
                end = i+1;
                break;
            }
        }
    }
    makeReverse(0,end);

}
void fix(int index){
    int end=0;
    for(int i =index; i<data.size(); i++){
        if(data[i].first!=data[index].first||i==data.size()-1){
            end = i+1;
            break;
        }
    }
    makeReverse(index,end);

}
void find(){
    for(int i =1;i<data.size(); i++){
       if(data[i-1].first!=data[i].first&&data[i-1].second!=data[i].second)fix(i);  
    }
}

int main(){
    int testCase;
    cin>>testCase;
    while(testCase--){
        int n;
        cin>>n;
        getInputSort(n);
        find();
        int answer;
        cin>>answer;
        for(int i =0; i<answer; i++){
            int tmp;
            cin>>tmp;
            cout<<data[tmp-1].first<<" "<<data[tmp-1].second<<endl;
        }
         vector<pair<int,int> >tmp;
         data = tmp;
    }
    return 0;
}
