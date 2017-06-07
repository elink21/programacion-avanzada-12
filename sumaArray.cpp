#include <iostream>
#include <vector>
using namespace std;

int sumaArray(vector<int> A,int i)
{
	if(i<A.size())
	{
		return A[i]+sumaArray(A,i+1);
	}
}

int main()
{
	vector <int> A;
	for(int i=0;i<10;i++)
		A.push_back(i);
	cout<<sumaArray(A,0);
}