#include<iostream>
void merge(int * arr,int l,int r){
    int mid=(r+l)/2;
    int * brr=new int[r+1];
    int l1=l,l2=mid+1,p=0,i;
    while(l1<=mid &&l2<=r)
    {
        if(arr[l1]>arr[l2]) 
            brr[p++]=arr[l2++];
        else 
            brr[p++]=arr[l1++];
    }
    if (l2==r+1) 
        for(i=l1;i<=mid;i++) brr[p++]=arr[i];
    else 
        for(i=l2;i<=r;i++) brr[p++]=arr[i];
    for(i=l,p=0;i<=r;i++)
        arr[i]=brr[p++];
    delete[] brr;
}

void sort(int *arr,int l,int r){
    if (r==l) return;
    int mid=(r+l)/2;
    sort(arr,l,mid);
    sort(arr,mid+1,r);
    merge(arr,l,r);
}

int main(){
    using namespace std;
    int a[]={2,1,3,4,1,2,3,5,6,4,3,2};
    int n=sizeof(a)/sizeof(a[0]);
    int l=0,r=n-1;
    sort(a,l,r);
    for(int e:a){
        cout<<e<<" ";
    }

}