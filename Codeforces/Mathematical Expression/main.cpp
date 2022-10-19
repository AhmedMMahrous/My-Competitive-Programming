#include <iostream>

using namespace std;

int main()
{
int a,b,c;

char operation,x;

cin>>a>>operation>>b>>x>>c;

if (operation=='+')
    if(a+b==c)
       cout<<"Yes";
    else
       cout<<a+b;


if (operation=='-')
    if(a-b==c)
       cout<<"Yes";
    else
       cout<<a-b;

if (operation=='*')
    if(a*b==c)
       cout<<"Yes";
    else
       cout<<a*b;



    return 0;
}
