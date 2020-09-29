#include <iostream>
#include <vector>
#include <typeinfo>
#include <string>
using namespace std;
class Krug_kvadrat
{
    public:
    string *name;
        Krug_kvadrat()
        {
            string *name2;
            *name2="Батыр>";
            this->name=name2;
            delete name2;
        }
        ~Krug_kvadrat()
        {
            delete name;
        }
};
class Krug : public Krug_kvadrat
{
    public:
        Krug()
        {
           string *name2;
            *name2="Курбанов";
            this->name=name2;
            delete name2;
        }
        ~Krug()
        {
            cout<<"denstruct derivative"<<endl;
        }
};
class Kvadrat : public Krug_kvadrat
{
    public:
        Kvadrat()
        {
            string *name2;
            *name2="Батырович";
            this->name=name2;
            delete name2;
        }
        ~Kvadrat()
        {
            cout<<"denstruct derivative"<<endl;
        }
};
void del(vector<Krug_kvadrat*> all)
{
    for(int i=0;i<all.size();i++)
        delete all[i];
}
int main()
{
    vector<Krug_kvadrat*> all;
    for(int i=0;i<1;i++)
    {
    all.push_back(new Krug_kvadrat);
    all.push_back(new Krug);
    all.push_back(new Kvadrat);
    }
    del(all);
    return 0;
}