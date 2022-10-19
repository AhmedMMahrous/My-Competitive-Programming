#include<iostream>
#include <cmath>
using namespace std;
int main()
{
    double x,y;
    cin>>x>>y;
    int Floor;
    Floor = floor(x/y);
    cout<<"floor "<<x<<" / " <<y<<" = "<<Floor<<endl;

    double Ceil;
    Ceil = ceil(x/y);
    cout<<"ceil "<<x<<" / " <<y<<" = "<<Ceil<<endl;

    double Round;
    Round = round(x/y);
    cout<<"round "<<x<<" / " <<y<<" = "<<Round<<endl;



return 0;
}
