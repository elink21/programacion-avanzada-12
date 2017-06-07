#include <iostream>
using namespace std;

long long int fibonacci(int n)
{
	if (n==0 or n==1)
	{
		return n;
	}
	return fibonacci(n-1)+fibonacci(n-2);
}

int main()
{
	cout<<fibonacci(7);
}