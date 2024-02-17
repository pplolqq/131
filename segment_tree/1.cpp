#include<iostream>
using namespace std;
#define N 100000
#define ll long long
ll a[N];
ll seg[N+1];
ll sum[N];
int main(){
    int n,m;
    cin>>n>>m;
    for(int i=0;i<n;i++) cin>>a[i];
    seg[0]=a[0];
    sum[0]=a[0];
    for(int i=1;i<n;i++){
        seg[i]=a[i]-a[i-1];
        sum[i]=sum[i-1]+a[i-1];
    }
    for(int i=0;i<m;i++){
        int op;
        cin>>op;
        if(op==1){
            int l,r,v;
            cin>>l>>r>>v;
            seg[l]+=v;
            seg[r+1]-=v;
        }
        if(op==2){
            int l,r;
            cin>>l>>r;
        }
    }
}