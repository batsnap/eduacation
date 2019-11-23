#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    float y;
    for(float i=0.55;i<=1.05;i+=0.05)
    {
        y=(sqrt(pow(sin(i/2),3))+pow(pow(exp(1.0),1.3*i)+pow(exp(1.0),-1.3*i),1/3))/(abs(i-(7/9)));
        cout<<"при i= "<<i<<" значение функции равно:"<<y<<endl;
    }
    return 0;
}