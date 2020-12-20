#include <vector>
using namespace std;

class Base
{
	public:
		int* a;
	Base():a(new int){*a=3;}
	virtual ~Base(){}
	virtual Base* copy(){return new Base(*this);}
	Base(const Base& o){ a=o.a;}
};

class Child:public Base
{
	public:
		float a;
	Child(){this->a=2.61;}
	virtual ~Child(){}
	virtual Child* copy() {return new Child(*this);}
	Child(const Child& o){a=o.a;};
};

class Child2:public Base
{
	private:
		char test[10] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'f'};

	public:
		char *test2=&this->test;
		Child2(){}
		virtual ~Child2(){}
		virtual Child2* copy() {return new Child2(*this);}
		Child(const Child2& o){this->test2=o.test2;};
};

int main()
{
	vector<Base*> father,mother;
	for(int i=0;i<3;i++){father.push_back(new Child);}
	for(int i=3;i<6;i++){father.push_back(new Child2);}

	for(int i=0;i<6;i++)
	{
		Base* obj=father[i];
		Base* new_obj=obj->copy();
		mother.push_back(new_obj);
	}
	for(int i=0;i<father.size();i++){delete father[i];}
	for(int i=0;i<mother.size();i++){delete mother[i];}	

	return 0;
}