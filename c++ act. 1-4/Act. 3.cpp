//Activity 3: Converting inches to feet and yard to inches//
//Programmer: Avah Denesse E. Ayop//
//Date: Sept.16,2022//

#include <iostream>
using namespace std;

int main()
{
	float yd,ft;
	float inches;
	
	cout << "Convert inches to ft\n";
	cout << "Type inches:";
	cin >> inches;
	ft=inches/12;
	cout << "The length in inches to ft is:" <<ft;
	cout << "\n\n";
	cout << "Convert yd to inches\n";
	cout << "Type yd:";
	cin >> yd;
	inches=yd*36;
	cout << "The length of yd to inches is:" <<inches;
	return 0;
}
