#include <iostream>
#include <string.h>
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
int len,i,j,check;
char str1[100];
char pushv;
char print,str2[100]={'\0'};
cout<<"Enter the string:\n";
cin.get(str1,100);
cout<<str1<<endl;
for(i=0;str1[i]!='\0';i++)
{
	pushv=str1[i];
	s.push(pushv);
}
cout<<"The reversed string:\n";
for(i=0;str1[i]!='\0';i++)
{print=s.pop();
 str2[i]=print;
}
cout<<str2;
check=strcmp(str1,str2);
if(check==0)
cout<<"\nGiven string is a palindrome";
else
cout<<"\nGiven string is not a palindrome";
return 0;
}
