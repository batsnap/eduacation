#include <iostream>
#include <vector>
#include <typeinfo>
using namespace std;
class kurbanov
{
    public:
        kurbanov()
        {
        }
        kurbanov(const char* one1)
        {
            cout<<one1<<endl;
        }
        virtual ~kurbanov()
        {
            cout<<typeid(*this).name()<<endl;
        }
};
class Batyr : public kurbanov
{
    public:
        Batyr(const char* one1)
        {
            cout<<one1<<endl;
        }
        ~Batyr()
        {
            cout<<typeid(*this).name()<<endl;
        }
};

int main()
{
    vector<kurbanov*> all;
    all.push_back(new kurbanov("kurbanov"));
    all.push_back(new Batyr("batyr"));
    for(int i=0;i<all.size();i++)
        delete all[i];
    return 0;
}