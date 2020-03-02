#include <iostream>
#include <vector>
#include <typeinfo>
using namespace std;
class kurbanov
{
    public:
        int *i;
        kurbanov():i(new int)
        {
            *i=11;
        }
        ~kurbanov()
        {
            cout<<"i принадлежит классу:"<<typeid(*i).name()<<endl;
            delete i;
        }
};
class Batyr : public kurbanov
{
    public:
        int *i1;
        Batyr():i1(new int)
        {
            *i1=12;
        }
        ~Batyr()
        {
            cout<<"i2222 принадлежит классу:"<<typeid(*i1).name()<<endl;
            delete i1;
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