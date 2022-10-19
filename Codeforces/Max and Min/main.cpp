#include <iostream>

using namespace std;

int main()
{
    int a,b,c;
    cin>>a>>b>>c;
    int answer = a;
    if( answer > b )
        answer = b;
    if ( answer > c )
        answer = c;
    cout<<answer<<" ";

    int var = a;
    if( var < b )
        var = b;
    if ( var < c )
        var = c;
    cout<<var;




    return 0;
}
