#include<iostream>
using namespace std;

int main() {
  int numberOfInt, 
    data[100], 
    numberOf1 = 0, 
    numberOf5 = 0, 
    numberOf10 = 0;

  cin >> numberOfInt;

  for(int i = 0; i < numberOfInt; i++) {
    cin >> data[i];
  }

  for (int i = 0; i < numberOfInt; i++) {
    if (data[i] == 1) {
      numberOf1++;
    } else if (data[i] == 5) {
      numberOf5++;
    } else if (data[i] == 10) {
      numberOf10++;
    }
  }

  cout << numberOf1 << endl << numberOf5 << endl << numberOf10 << endl;

}
