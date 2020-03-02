#include <iostream>
#include <vector>
#include <typeinfo>
using namespace std;
class kurbanov
{
    public:
        kurbanov()
        {
            cout<<"construct base"<<endl;
        }
        virtual ~kurbanov()
        {
            cout<<"destruct base"<<endl;
        }
};
class Batyr : public kurbanov
{
    public:
        Batyr()
        {
            cout<<"construct derivative"<<endl;
        }
        ~Batyr()
        {
            cout<<"denstruct derivative"<<endl;
        }
};
void del(vector<kurbanov*> all)
{
    for(int i=0;i<all.size();i++)
        delete all[i];
}
int main()
{
    vector<kurbanov*> all;
    for(int i=0;i<1;i++)
    {
    all.push_back(new kurbanov);
    all.push_back(new Batyr);
    }
    del(all);
    return 0;
}