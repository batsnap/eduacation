#include <iostream>
using namespace std;

int main(){
    int x=1;
    a:
    {
        cout<<x<<endl;
        x++;
        goto a;
    }
    return 0;
}