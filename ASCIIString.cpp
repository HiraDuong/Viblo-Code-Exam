// C++ implementation of the approach
#include <bits/stdc++.h>
using namespace std;

// Function to print the character sequence
// for the given ASCII sentence
void asciiToSentence(string str, int len)
{
	int num = 0;
	for (int i = 0; i < len; i++) {

		// Append the current digit
		num = num * 10 + (str[i] - '0');

		// If num is within the required range
		if (num >= 32 && num <= 122) {

			// Convert num to char
			char ch = (char)num;
			cout << ch;

			// Reset num to 0
			num = 0;
		}
	}
}

// Driver code
int main()
{
	int T;
    cin>>T;
    string s;
    for(int i = 0;i<T;i++){
        cin>>s;
        int len = s.size();
	    asciiToSentence(s, len);\
        cout<<endl;
    }

	return 0;
}
