#include <iostream>
using namespace std;
int main()
{
        int a,b;
        char operation;
        cin>>a >>operation>> b;

        if (operation=='<' && a<b)
           cout<<"Right";
        else if(operation=='>' && a>b)
            cout<<"Right";
        else if (operation=='>' && a>b)
            cout<<"Right";
        else if (operation=='=' && a==b)
            cout<<"Right";
        else
            cout<<"Wrong";



    return 0;

    }
