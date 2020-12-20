/*1 задание
Задать два иерархически связанных полиморфных класса: деталь и сборка 
(один из них базовый). Все конструкторы находятся в зоне protected 
(чтобы запретить явное создание).В main() следует создать несколько 
экземпляров указанных типов, помещая их в хранилище (vector), 
используя шаблонную дружественную функцию. 
Дополнить программу всем необходимым для ее правильной работы. 
*/
#include <iostream>
#include <vector>
using namespace std;

class detail
{
protected:

	int a=314;

	 detail& operator=(const int& a);
	
	 virtual ~detail() 
	 { 
		 delete& a; 
	 }
};

detail& detail::operator=(const int& a)
{
	detail b;
	b.a = a;
	return b;
}


class assembly : public detail
{
protected:
	double a = 3.14;
	assembly& operator=(const int& a);
	~assembly() 
	{ 
		delete& a; 
	}
};

int main()
{
	vector <detail*> v1;

	v1.push_back(new detail());
	v1.push_back(new assembly());
	return 0;
}
