#include <iostream>
using namespace std;

int CB(int n, int k)
{
	if (k==0 or n==k)
	{
		return 1;
	}
	else{
		return CB(n-1,k-1)+CB(n-1,k);
	}
}

int main()
{
	cout<<CB(5,2);
}