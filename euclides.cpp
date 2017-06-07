#include <iostream>
using namespace std;

float mcd(int m, int n)
{
	if (n==0)
	{
		return m;
	}
	else return  mcd(n,m%n);

}


int main()
{
	cout<<mcd(12,40);
}