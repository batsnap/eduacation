#include <iostream>
#include <cmath>
using namespace std;
void func(float x)
{
    float s;
    float expmy=pow(exp(1.0),1.3*x)+pow(exp(1.0),-1.3*x);
    s=(sqrt(pow(sin(x/2),3))+pow(expmy,1/3))/(abs(x-(7/9)));
    cout<<"при i= "<<x<<" значение функции равно:"<<s<<endl;
};
int main()
{
    for(float i=0.55;i<=1.05;i+=0.05)
    {
        func(i);
    }
    return 0;
}