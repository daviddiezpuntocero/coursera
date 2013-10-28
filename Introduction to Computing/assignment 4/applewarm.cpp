#include<iostream>
#include<math.h>
using namespace std;

int main() {
  double total, speed, time;
  int result;
  cin >> total >> speed >> time;
  result = floor(total - (time/speed));
  if (result <= 0) {
    cout << 0;
  } else {
    cout << result;
  }
}
