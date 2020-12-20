#include <vector>
using namespace std;

class Parent
{
	public:
		float* a;
	Parent():a(new float){*a=3.14;}
	virtual ~Parent(){}
	virtual Parent* copy(){return new Parent(*this);}
	Parent(const Parent& o){ a=o.a;}
};

class Child:public Parent
{
	public:
	Child(){}
	virtual ~Child(){}
	virtual Child* copy() {return new Child(*this);}
	Child(const Child& o);
};
int main()
{
	vector<Parent*> father,mother;
	for(int i=0;i<3;i++){father.push_back(new Parent);}
	for(int i=0;i<3;i++)
	{
		Parent* obj=father[i];
		Parent* new_obj=obj->copy();
		mother.push_back(new_obj);
	}
	for(int i=0;i<father.size();i++){delete father[i];}
	for(int i=0;i<mother.size();i++){delete mother[i];}	

	return 0;
}