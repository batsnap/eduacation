#include <iostream>
using namespace std;
int main()
{
    int n;
    float s;
    cin>>n;
    s=2.0;
    for (int i=1; i<n;i++)
    {
        s=1+1/s;
    }
    cout<<s<<endl;
    return 0;
}