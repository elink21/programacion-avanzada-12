#include <iostream>
using namespace std;

int particion(int m,int n)
{
	if(m==1 or n==1) return 1;
	if (m<n)return particion(m,m);
	if ( m==n ) return 1+particion(	m-1,m);
	if (m>n) return particion(m,n-1)+particion(m-n,n);
}


int main()
{
	cout<<particion(6,6);
}