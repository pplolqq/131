#include<iostream>
using namespace std;
class person{
public:
    void show(){
        cout<<"name:"<<name<<endl;
        cout<<"did:"<<did<<endl;
    }
private:
    int name=1;
    float did=35;
};
template <typename T>
void print (const T &t){
    cout<<t<<endl;
}
int main(){
    person s;
    // int * p=(int*)&s;
    float*p1=(float*)&s;
    int * p2=(int*)p1;
    // float *p2=&s.did;
    float *newp=(p1+1);
    *newp=13;
    *p2=11;
    s.show();
    // cout<<*newp;    
}