#include <iostream>
using namespace std;

int main()
{
    int a=0;
    int *s= new int[1];
    int *s1;
    int sizeS=0;
    while (a>=0)
    {
        cout<<"Введите число:";
        cin>>a;
        if (a<0)
            break;
        if (sizeS==0)
        {
            s[sizeS]=a;
            cout<<s[sizeS];
            sizeS++;
        }
        else
        {
            s1= new int[sizeS +1];
            for(int i=0;i<sizeS;i++)
            {
                s1[i]=s[i];
            }
            s1[sizeS]=a;
            delete [] s;
            s= new int[sizeS+1];
            for(int i=0;i<sizeS+1;i++)
            {
                s[i]=s1[i];
                cout<<s[i]<<" ";
            }
            delete [] s1;
            sizeS++;
        }
        cout<<endl;
        
    }
    delete [] s;
    return  0;
}