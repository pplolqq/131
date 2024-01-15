#include<iostream>
#include<cmath>
struct Point{
    int x=0;
    int y=0;
    bool isend();
    bool isok();
    void add(const Point &);
};
Point horse,End;
Point move[2]={{1,0},{0,1}};
bool Point::isok(){
    int dy=fabs(x-horse.x);
    int dx=fabs(y-horse.y);
    int p=dx+dy;
    int p1=fabs(dx-dy);
    if (p==3 && (dx==1|| dy==1) || p==0){
        return false;
    }
    if(x>End.x || y>End.y){
        return false;
    }
    return true;
}
bool Point::isend(){
    return x==End.x && y==End.y;
}
void Point::add(const Point & other){
    x+=other.x;
    y+=other.y;
}
int res=0;
void search(Point init){
    if (init.isend()){
        res+=1;
        return;
    }
    Point t=init;
    for(int i=0;i<2;i++){
        init.add(move[i]);
        if(init.isok()){
            search(init);
        }
        init =t;
    }
}
int main(){
    using namespace std;
    cin>>End.x>>End.y;
    cin>>horse.x>>horse.y;
    search(Point{0,0});
    cout<<res;
}