#include<iostream>
#include<string>
using namespace std;
int index[4];
int gear[4][8];
void test(){
    for(int i =0; i<4; i++){
        for(int j=0; j<8; j++){
            cout<<gear[i][(index[i]+j)%8];
        }   cout<<endl;
    }
}
void getInput(){
    string line;
    for(int i =0; i<4; i++){
        cin>>line;
        for(int j=0; j<8; j++){
            gear[i][j]=line[j]-48;
        }
    }
}
void tuneGear(int s, int flag){
    int t = s-1;
    int f = flag;   
    bool sectA = gear[0][index[0]+2]^gear[1][(index[0]-2)%8];
    bool sectB = gear[1][index[0]+2]^gear[2][(index[0]-2)%8];
    bool sectC = gear[2][index[0]+2]^gear[3][(index[0]-2)%8];
    index[t] = (index[t]-flag+8)%8;
    if(t==0&&sectA){
        f *= -1;
        index[t+1] = (index[t+1]-f)%8;
        t++;
        sectA = !sectA;
    }
    if((t==1&&sectA)||(t==2 && sectB) ){
        f *= -1;
        index[t-2] = (index[t-2]-f)%8;
        if(sectA&&t==2){
            f*=-1;
            index[t-3] = (index[t-3]-f)%8;
        }

    }
    if((t==1&&sectB)||(t==2&& sectC)){
        f *= -1;
        index[t+1] = (index[t+1]-f)%8;
        t++;
        if(sectB)sectB = !sectB;
        if(sectC)sectC = !sectC;
    }
    if(t==3&&sectC){
        f *= -1;
        index[t-2] = (index[t-2]-f)%8;
        if(sectB&&t==3){
            f *= -1;
            index[t-3] = (index[t-3]-f)%8;
        }
        if(sectA&&sectB){
            f *= -1;
            index[t-4] = (index[t-4]-f)%8;
        }

    }

}



int main(){
    getInput();
    int t;
    cin>>t;
    while(t--){
        int s, flag;
        cin>> s>>flag;
        tuneGear(s,flag);
    }
    test();
    
    return 0;

}
