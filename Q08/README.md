Monoton walkway
===
### 백준 11067
```
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
```

---
규칙은 찾기 쉬웠으나 구현이 조금 까다 로웠다. (안쓰던 자료구조 때문에) 방향이 직선 혹은 90도 회전 밖에 안되기 때문에 같은 x좌표에 있는 선들은 일직선이며 다음 x 좌표로 나아가는 점은 목표 x 좌표와 y좌표가 갖게 정렬해주면 된다. 정렬 순서만 맞추고 하나의 벡터에 넣어주면 random access로 접근할 수 있다.

---
c++의 pair 객체와 python의 dict가 알맞은 자료 구조로 사용 될 수 있다. 
pair 객체 사용 법 : https://www.evernote.com/shard/s651/sh/0cd870ec-24e7-4890-b5b0-7f8f3efdadc1/4adf76014f893abf21974436d9e8e667
---

python 및 자바로도 구현해보자.
