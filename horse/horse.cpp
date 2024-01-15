#include<iostream>
#include<cmath>
long long record[40][40]={0};
int horse[2];
bool isok(int x,int y){
    if(x<0 || y<0){
        return false;
    }
    int dx=fabs(horse[0]-x);
    int dy=fabs(horse[1]-y);
    int p=dx+dy;
    if(p==3 &&(dx==1 ||dy==1) || p==0){
        return false;
    }
    return true;
}
long long  search(int x,int y){
    if(record[x][y] !=0){
        return record[x][y];
    }
    if(! isok(x,y)){
        return 0;
    }
    if (x==0 && y==0){
        return 1;
    }
    long long res=search(x-1,y)+search(x,y-1);
    record[x][y]=res;
    return res;
}
int main(){
    using namespace std;
    int x,y;
    cin>>x>>y;
    cin>>horse[0]>>horse[1];
    cout<<search(x,y);
}

