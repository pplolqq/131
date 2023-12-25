#include <iostream>
#include<stdlib.h>
using namespace std;
const int n=6;
int res[n][n];
struct dir{
    int x;
    int y;
};
struct pos{
    int r;
    int c;
    bool is_ok(dir & to);
    void add(dir & to);
};
void pos::add(dir & to){
    r+=to.x;
    c+=to.y;
}
bool pos::is_ok(dir & to){
    int r1=r+to.x;
    int c1=c+to.y;
    return r1>=0 && r1<n && c1>=0 && c1<n && res[r1][c1]==0;
}
dir to[4]={{0,1},{1,0},{0,-1},{-1,0}};
pos now={0,-1};
int main(){
    int idx=0;
    for(int i=1;i<=n*n;i++){
        if(! now.is_ok(to[idx])){
            idx+=1;
            idx%=4;
        }
        now.add(to[idx]);
        res[now.r][now.c]=i;
    }
    void printout(int a[n][n]);
    printout(res);
    // cout<<a[0];
}
void printout(int a[n][n]){
    for(int r=0;r<n;r++){
        for(int c=0;c<n;c++){
            printf("%-4d",a[r][c]);
        }
        cout<<endl;
    }
}