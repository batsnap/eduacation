#include <iostream>
#include <vector>
#include <typeinfo>
using namespace std;
class kurbanov
{
    public:
        int *i;
        float *a;
        kurbanov():i(new int),a(new float)
        {
            *i=11;
            *a=3.14;
        }
        ~kurbanov()
        {
            cout<<"i принадлежит классу:"<<typeid(*i).name()<<endl;
            delete i;
            delete a;
        }
};
class Batyr : public kurbanov
{
    public:
        int i1;
        float *a;
        Batyr():a(new float)
        {
            i1=12;
            *a=10.3;
        }
        ~Batyr()
        {
            cout<<"i2222 принадлежит классу:"<<typeid(*i1).name()<<endl;
            delete i1;
            delete a;
        }
};

int main()
{
    vector<kurbanov*> all;
    all.push_back(new kurbanov);
    all.push_back(new Batyr);
    for(int i=0;i<all.size();i++)
        delete all[i];
    return 0;
}