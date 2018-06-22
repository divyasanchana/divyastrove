#include <iostream>
#include <string>
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
void display();
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

void stack :: display()
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
int len,i;
string str1;
char pushv;
cout<<"Enter the length of the string\n";
cin>>len;
cout<<"Enter the string:\n";
getline(cin,str1);
cout<<str1;
for(i=0;i<len;i++)
{
	pushv=str1[i];
	s.push(pushv);
	cout<<pushv<<" was successfully pushed\n";
}
cout<<"The reversed string:\n";
s.display();
return 0;
}
