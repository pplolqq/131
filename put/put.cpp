#include<iostream>
using namespace std;
int a[10000][4];
int main(){
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        for(int j=0;j<4;j++){
            cin>>a[i][j];
        }
    }
    int p[2];
    cin>>p[0]>>p[1];
    int res=0;
    int flag=0;
    for(int i=0;i<n;i++){
        int dx=p[0]-a[i][0];
        int dx2=a[i][2]-dx;
        int dy=p[1]-a[i][1];
        int dy2=a[i][3]-p[1];
        if(dx>=0 && dx2<=0 && dy>=0 && dy2<=0){
            res=i;
        }
    }
    if(flag){
        cout<<res+1;    
    }
}