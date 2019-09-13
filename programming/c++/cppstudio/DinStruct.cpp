#include <iostream>
#include <string.h>
using namespace std;
struct nameages
{
    int age;
    char name [10];
};

int main()
{
    int k=1;
    int c=1;
    nameages *p= new nameages[1];
    while (k)
    {
        if (c==1)
        {
            cout<<"Имя:";
            cin>>p[c-1].name;
            cout<<"Возраст:";
            cin>>p[c-1].age;
            cout<<"Элементы структуры: "<<p[c-1].name<<", "<<p[c-1].age<<endl;
        }
        else
        {
            nameages *copy=new nameages[c-1];
            for(int i=0;i<c-1;i++)
            {
                strcpy(copy[i].name,p[i].name); 
                copy[i].age=p[i].age;
            }
            delete [] copy;

            p= new nameages[c];

            for(int i=0;i<c-1;i++)
            {
                strcpy(p[i].name,copy[i].name); 
                p[i].age=copy[i].age;
            }

            cout<<"Имя:";
            cin>>p[c-1].name;
            cout<<"Возраст:";
            cin>>p[c-1].age;

            for(int i=0;i<c;i++)
            {
                cout<<"Элементы структуры: "<<p[i].name<<", "<<p[i].age<<endl;
            }
            
        }
        c++;
        cout<<"Ввести данные еще раз-1; закончить ввод-0:";
        cin>>k;
    }
    delete [] p;
    return 0;
}