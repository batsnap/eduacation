#include <iostream>
using namespace std;

int foo(int k)
{
    int c=k*k;
    if (k!=0)
    {
        return foo(k)*foo(k-1);
    }
}
int main()
{
    int c;
    cin>>c;
    cout<<foo(c)<<endl;
    return 0;
}
