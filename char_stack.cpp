#include <iostream>
using namespace std;

class stack
{
public:
int check;
int i;
char element;
int top=-1;
char a[50];
char push(char);
char pop();
int empty();
int overflow();
void display(int);
};

char stack :: push(char letter)
{
check=overflow();
if(check==1)
cout<<"Stack Overflow";
else
{
	top=++top;
	a[top]=letter;
}
}

char stack :: pop()
{
check=empty();
if(check==1)
cout<<"Stack is empty";
else
{
	element=a[top];
	top=--top;
}
	return element;
}

void stack :: display(int n)
{
for(i=top;i>=0;i--)
cout<<a[i]<<endl;
}

int stack :: empty()
{
if(top==-1)
return 1;
else
return 0;
}

int stack :: overflow()
{
if(top==50)
return 1;
else
return 0;
}

int main() 
{
stack s;
char letter;
char d;
int length;
int choice;
cout<<"Enter the number of characters (less than or equal to 50):\n";
cin>>length;
do
{
cout<<"1=Push\n2=Pop\n3=Display\n4=Exit\n";
cout<<"Enter the choice:\n";
cin>>choice;
	switch(choice)
	{
		case 1:
		cout<<"Enter the element to be pushed\n";
		cin>>letter;
		s.push(letter);
		cout<<letter<<" was successfully pushed\n";
		break;
		
		case 2:
		d=s.pop();
		cout<<d<<" was successfully popped\n";
		break;
		
		case 3:
		s.display(length);
		break;
		
		case 4:
		break;
		
		default:
		cout<<"Enter valid choice\n";
	}
}while(choice!=4);
return 0;
}
		
	
