#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
    cout << fixed << setprecision(9);
    double x = 3.141592653;
    double R ,area;
    cin>>R;
    area = x *(R*R);
    cout << area << setprecision(9);


return 0;
}
