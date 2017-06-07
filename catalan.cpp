#include <iostream>
using namespace std;

long long int factorial(int n)
{
	if(n==0 or n==1)
	{
		return n;
	}
	else return n*factorial(n-1);
}


long long int catalan(int n)
{
	return (factorial(2*n) ) / (factorial(n)*factorial(n+1));
}


int main()
{
	cout<<catalan(5);
}