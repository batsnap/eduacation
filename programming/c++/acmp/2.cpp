#include <iostream>

using namespace std;

int a,sum;

int main(){
    sum=0;
    cin >> a;
    if (a>0)
    {
        sum=((a+1)*a)/2;
    }
    else if (a<0)
    {
        for (int i=a;i<2;i++)
            sum+=i;
    }
    else
    {
        sum=1;
    }
    cout<<sum<<endl;
    return 0;
}