#include <iostream>
#include <set>
using namespace std;

class Kurbanov
{
public:
	int* k;
	Kurbanov():k(new int)
	{
		*k=5;	
	}
	virtual Kurbanov* clone()
	{
		Kurbanov *p=new Kurbanov;
		p->k=k;
		return p;
	}
	
	virtual ~Kurbanov();
	
};
class Batyr:public Kurbanov
{
public:
	float c;
	Batyr()
	{
		this->c=2.61;
	}
	virtual Kurbanov* clone()
	{
		Batyr *p=new Batyr;
		p->c=c;
		return p;
	}
	~Batyr();
	
};
int main(int argc, char const *argv[])
{
	set<Kurbanov*> k1;
	set<Kurbanov*> k2;
	k1.insert(new Kurbanov);
	k1.insert(new Batyr);
	for (auto i:k1) //set<Kurbanov*>::iterator it=k1.begin(); it!=k1.end();++it не рабоатет( пришлось использовать auto(
	{
		Kurbanov *ptr=i->clone();
		k2.insert(ptr);	
	}
	
	return 0;
}