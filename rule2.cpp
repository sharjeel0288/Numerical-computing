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

bool isValidIMEI(int_fast32_t n)
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
    int_fast32_t imei;
    again:
    cout<<"Enter imei : ";
    //cin>>imei;
	imei=350098039274908;
    int i, arr[15];
	

//	if (isValidIMEI(imei))

		{
            for ( i = 14; i >=0; i--)
            {
               int n=imei%10;
               arr[i]=n;
               imei=imei/10;
            }
                if (imei == 0 && i>0)
                {
                    cout<<"invalid IMEI"<<endl;
                    goto again;
                }
            for ( i = 0; i < 7; i++)
            {
                cout<<abs((arr[i]*arr[14-i])%10);
            }
			cout<<endl;
			for ( i = 0; i < 7; i++)
            {
                cout<<abs((arr[i]*7)%10);
            }
			cout<<endl;
			for ( i = 0; i < 7; i++)
            {
                cout<<abs((arr[i]*arr[(2*i)%15])%10);
            }
			cout<<endl;
           // cout<<arr[i];
            
        }
	//else
		// cout << "Invalid IMEI Code";
	// getchar();
	cout<<endl<<"23793328";
	return 0;
}

// This code is contributed by Yash_R
