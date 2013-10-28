#include<iostream>
#include<math.h>
using namespace std;

int main() {
  double h, r, w = 20, PI = 3.14159;

  cin >> h >> r;

  cout << ceil (w/(r/10*r/10*PI*h/10));
}
 
