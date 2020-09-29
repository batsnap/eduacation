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
			k++;
	}
	return k;
}
int count_of_art_books (vector<library*> lib) //function count of art books
{
	int k=0; //amount of technical books
	for(int i=0;i<lib.size();i++)
	{
		if (lib[i]->type_book=="art") 
			k++;
	}
	return k;
}
/*void output_amount_of_books_switch(vector<library*> lib)
{
	string type;
	cout<<"Select the number of the book you want to learn";getline(cin,type);
	switch(type)
	{
		case "tech":
			cout<<count_of_tech_books(lib);
			break;

		case "art":
			cout<<count_of_art_books(lib);
			break;

		default:
			break;

	}
}*/
void output_amount_of_books(vector<library*> lib)
{
	string type;
	cout<<"Select the number of the book you want to learn";getline(cin,type);
	if (type=="tech")
	 	cout<<count_of_tech_books(lib);
	else if (type=="art")

			cout<<count_of_art_books(lib);
	
}

//main part
int main()
{
	int action;
	int amount_of_books;
	vector<library*> lib;
	while(true)
	{
		cout<<"Choose action:\n1)add book\n2)print amount of books(using switch)\n3)print amount of books\nprint noumber(1-3):\t";
		cin>>action;
		if (action==1)
		{
			cout<<"input amount of books:";cin>>amount_of_books;
			add_book(lib,amount_of_books);
		}
		/*else if (action==2)
		{
			output_amount_of_books_switch(lib);
		}*/
		else if (action==3)
		{
			output_amount_of_books(lib);
		}

	}
	return 0;
}