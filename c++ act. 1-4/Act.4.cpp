//Activity 4: Converting Celsius to Fahrenheit and Fahrenheit to Celsius//
//Programmer: Avah Denesse E. Ayop//
//Date: Sept.20,2022//

#include <iostream>
using namespace std;

int main()
{
	float c,f;
	
	cout << "Convert Celsius to Fahrenheit\n";
	cout << "Type Celsius:";
	cin >> c;
	f=c*1.8 + 32;
	cout << "The Tempurature in Fahrenheit is:" << f;
	cout << "\n\n";
	
	cout << "Convert Fahrenheit to Celsius\n";
	cout << "Type Fahrenheit:";
	cin >> f;
	c=(f-32) *5/9;
	cout << "The Temperature in Celsius is:" << c;
	return 0;

}
