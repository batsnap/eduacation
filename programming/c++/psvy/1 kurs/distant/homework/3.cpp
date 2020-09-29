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
        ~kurbanov()
        {
        }
        virtual void print()
        {
        }
};
class child_1 : public kurbanov
{
    public:
    const char *a1[100];
        child_1(const char *a)
        {
            *a1=a;
        }
        ~child_1()
        {
            delete *a1;
        }
        void print() override
        {
            cout<<*a1<<endl;
        }
};
class child_2 : public kurbanov
{
    public:
    const char *a1[100];
        child_2(const char *a)
        {
            *a1=a;
        }
        ~child_2()
        {
            delete *a1;
        }
        void print() override
        {
            cout<<*a1<<endl;
        }
};
void del(vector<kurbanov*> &all)
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
    all.push_back(new child_1("char"));
    all.push_back(new child_2("char2"));
    }
    all[1]->print();
    all[2]->print();
    del(all);
    cout<<"Память очищена"<<endl;
    return 0;
}