#include <iostream>
#include <vector>
using namespace std;

class base
{
    public:
        int *mas=new int[10];
    virtual void print()
        {
            for(int i=0;i<10;i+=2)
                cout<<mas[i]<<"\t";
            cout<<endl;
        }
};
class nobase: public base
{
    public:
    void print() override
        {
            for(int i=1;i<10;i+=2)
                cout<<this->mas[i]<<"\t";
            cout<<endl;
        }
};
void create(vector<base*> mas)
{
    mas.push_back(new base);
    mas.push_back(new nobase);
}
void init(vector<base*> mas1)
{
    int k=100;
    for(int i=0;i<mas1.size();i++)
        {
            for(int j=0;j<10;j++)
            {
                
                mas1[i]->mas[j]=k;
                k+=3;
            }
        }
}
void del(vector<base*> mas)
{
    for(int i=0;mas.size();i++)
        delete mas[i];
}
int main()
{
    vector<base*> mas;
    create(mas);
    init(mas);
    for(int i=0;i<mas.size();i++)
    {
        mas[i]->print();
        cout<<i<<"\t";
        cout<<endl;
    }
    del(mas);
    return 0;
}