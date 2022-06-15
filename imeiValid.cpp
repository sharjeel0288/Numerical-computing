// C++ program to check whether the
// given EMEI number is valid or not.
#include<bits/stdc++.h>
using namespace std;

// Function for finding and returning
// sum of digits of a number
int sumDig(int n)
{
	int a = 0;
	while (n > 0)
	{
		a = a + n % 10;
		n = n / 10;
	}
	return a;
}

bool isValidIMEI(long n)
{
	
	// Converting the number into
	// String for finding length
	string s = to_string(n);
	int len = s.length();

	if (len != 15)
		return false;

	int sum = 0;
	for(int i = len; i >= 1; i--)
	{
	int d = (int)(n % 10);
		
	// Doubling every alternate digit
	if (i % 2 == 0)
		d = 2 * d;
			
	// Finding sum of the digits
	sum += sumDig(d);
	n = n / 10;
	}
	
	return (sum % 10 == 0);
}

// Driver code
int main()
{
	// 15 digits cannot be stored
	// in 'int' data type
	long n = 490154203237518L;

	if (isValidIMEI(n))
		cout << "Valid IMEI Code";
	else
		cout << "Invalid IMEI Code";
	
	return 0;
}

// This code is contributed by Yash_R
