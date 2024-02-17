#include<iostream>
// using namespace std;

void swap(int &a,int &b){
    int t=a;
    a=b;
    b=t;
}

// using namespace std;

// void quick_sort(int *arr,int l,int r){
//     if(r<=l) return;
//     int mid=arr[l];
//     int p=l,q=l;
//     while(q++<r){
//         if(arr[q]<mid ){
//             swap(arr[q],arr[++p]);
//         }
//     }
//     swap(arr[l],arr[p]);
//     quick_sort(arr,l,p-1);
//     quick_sort(arr,p+1,r);
// }
// int main(){
//     int a[]={4,2,1,7,8,1,5,3,1};
//     int n=sizeof(a)/sizeof(a[0]);
//     quick_sort(a,0,n-1);
//     for(int i:a){
//         cout<<i<<" ";
//     }
// }
void quick_sort(int *arr,int l,int r){
    // int mid=rand()%(r-l);
    int mid=0;
    int pl=l,pr=r;
    // quick_sort(arr,l,pl);
}
using namespace std;
int main(){
    int arr[]={5,7,1,1,1,1,1};
    int n=sizeof(arr)/sizeof(arr[0]);
    quick_sort(arr,0,n-1);
    for(int e:arr){
        cout<<e<<endl;
    }
}
