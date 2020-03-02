#include <iostream>
#include <vector>
#include <typeinfo>
using namespace std;
class kurbanov
{
    public:
        float *i;
        unsigned long* i1;
        kurbanov():i(new float),i1(new unsigned long)
        {
            *i=11.0;
            *i1=5;
        }
        ~kurbanov()
        {
            delete i,i1;
        }
};
class Batyr : public kurbanov
{
    public:
        float *i;
        unsigned long* i1;
        Batyr():i(new float),i1(new unsigned long)
        {
            *i=12.0;
            *i1=5;
        }
        ~Batyr()
        {
            delete i1,i;
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