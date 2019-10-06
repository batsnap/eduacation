#include <iostream>
using namespace std;

int main()
{
    bool variant=true;
    int ans=0;
    do
    {
        cin>>ans;
        switch(ans)
        {
            case 1:
                cout<<"1 floar"<<endl;
                break;
            case 2:
                cout<<"2 floar"<<endl;
                break;
            case 3:
                cout<<"3 floar"<<endl;
                break;
            case 4:
                cout<<"4 floar"<<endl;
                break;
            case 5:
                cout<<"5 floar"<<endl;
                break;
            default:
                variant=false;
        }
    }
    while (variant);
    return 0;
}