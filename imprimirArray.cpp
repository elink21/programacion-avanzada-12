#include <iostream>
#include <vector>
using namespace std;

void imprimirArray(vector<int> A,int i)
{
	if(i<A.size())
	{
		cout<<A[i]<<"\t";
		imprimirArray(A,i+1);
	}
}

int main()
{
	vector <int> A;
	for(int i=0;i<10;i++)
		A.push_back(i);
	imprimirArray(A,0);
}