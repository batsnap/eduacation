/*2 задание
Задать два иерархически связанных полиморфных класса: Base и Derived. 
В главной функции программы последовательно выполняется два действия. В цикле случайно 
(random) создаются несколько экземпляров любого из заданных типов (например, по четному 
случайному числу создается Base, а по нечетному - Derived). После создания объектов, 
их копии передаются в функцию add, которая помещает их в общее хранилище.
Затем в main необходимо показать для каждого из имеющихся в хранилище объектов разницу 
в поведении их типа, доставая их по очереди из хранилища. 
В заключении, освободить все ресурсы.*/
#include <cstdlib>
#include <vector>
#include <ctime>
#include <iostream>
#include <typeinfo>
using namespace std;

class Base
{
public:
	Base(){};
	~Base(){};
	
};
class Derived:public Base
{
public:
	Derived(){};
	~Derived(){};
	
};
int main()
{
	int k;
	srand(time(0));
	vector<Base*> v1,v2;
	for(int i=0;i<5;i++)
	{
		k=rand()%100;
		if (k%2==0)
			v1.push_back(new Base);
		else
			v1.push_back(new Derived);
		cout<<k<<"\t"<<typeid(*v1[i]).name()<<endl;
	}
	
	return 0;
}