#include <iostream>

using namespace std;

int main()
{

 long int a,b,c,d;
cin>>a>>b>>c>>d;
long int f=((a%100)*(b%100))%100;
long int k=((c%100)*(d%100))%100;
long l=((f%100)*(k%100))%100;
if(l<=9)cout<<0<<l;
else cout<<l;

return 0;

}


