//connect the necessary libraries
#include <vector>
#include <iostream>
#include <string>
using namespace std;

//make class
class library
{
	public:
		string name_author;
		string name_book;
		string type_book;
		library()//constructor default
		{
		}

		library(string name_autor1, string name_book1, string type_book1)//constructur with parametrs
		{
			this->name_author=name_autor1;
			this->name_book=name_book1;
			this->type_book=type_book1;
		}
		~library()//destructor
		{
		}
};

void add_book(vector<library*> &lib, int amount)//function to add books to your library
{
	string name_author;
	string name_book;
	string type;
	for(int i=0;i<amount;i++)
	{
		cout<<"input name of author:\t";	getline(cin,name_author);
		cout<<"input name of book:\t";		getline(cin,name_book);
		cout<<"input type of book\t";		getline(cin,type);
		cout<<endl;
		lib.push_back(new library(name_author,name_book,type));
	}
}
int count_of_tech_books (vector<library*> lib) //function count of techical_books
{
	int k=0; //amount of technical books
	for(int i=0;i<lib.size();i++)
	{
		if (lib[i]->type_book=="tech") 
		{
			k++;
		}
	}
	return k;
}

int count_of_art_books (vector<library*> lib) //function count of art books
{
	int k=0; //amount of technical books
	for(int i=0;i<lib.size();i++)
	{
		if (lib[i]->type_book=="art")
		{
			k++;
		}
	}
	return k;
}

void output_amount_of_books_switch(vector<library*> lib)
{
	int type1;
	cout<<"Select the genre of the book you want to learn\n1-tech\n2-art:\t";
	cin>>type1;

	switch(type1)
	{
		case 1:
			cout<<count_of_tech_books(lib)<<endl;
			break;
		case 2:
			cout<<count_of_art_books(lib)<<endl;
			break;
		default:
			break;

	}
}
void output_amount_of_books(vector<library*> lib)
{
	string type;
	cout<<"Select the genre of the book you want to count:\t";
	getline(cin,type);
	if (type=="tech")
	{
	 	cout<<count_of_tech_books(lib)<<endl;
	}
	else if (type=="art")
	{	
		cout<<count_of_art_books(lib)<<endl;
	}
	
}
void print_all_books(vector<library*> lib)
{
	for(int i=0;i<lib.size();i++)
	{
		cout<<lib[i]->name_author<<endl;
		cout<<lib[i]->name_book<<endl;
		cout<<lib[i]->type_book<<endl;
	}
}

//main part
int main()
{
	string action;
	bool end=true;
	int amount_of_books;
	vector<library*> lib;
	while(end)
	{
		cout<<"Choose action:\n1)Add books\n2)Print amount of books(using switch)\n3)Print amount of books\n4)End programm\nPrint noumber(1-3):\t";
		getline(cin,action);
		if (action=="1")
		{
			cout<<"input amount of books:\t";cin>>amount_of_books;
			add_book(lib,amount_of_books);
		}
		else if (action=="2")
		{
			output_amount_of_books_switch(lib);
		}
		else if (action=="3")
		{
			output_amount_of_books(lib);
		}
		else if (action=="4")
		{
			end=false;
		}

	}

	return 0;
}