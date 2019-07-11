#include <iostream>
#include <cstdlib>
using namespace std;
int main()
{   
    int n;
    cin >> n;
    int k[n];
    for(int i=0;i<=n;i++)
    {   
        k[i]=rand()%7;
    }
    for (int i=0; i<=n;i++)
    {
        cout <<k[i]<<" ";
    }
    cout<<endl;
    return 0;
}