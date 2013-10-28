#include<iostream>
#include<math.h>
using namespace std;

int main() {
  int input, a, b, c;
  cin >> input;
  a = floor(input/100);
  b = floor((input - 100 * a)/10);
  c = input - a * 100 - b * 10;
  cout << a << "\n" << b << "\n" << c;
}
