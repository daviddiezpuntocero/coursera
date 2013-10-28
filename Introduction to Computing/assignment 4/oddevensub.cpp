#include<iostream>
using namespace std;

int main() {
  int odd = -1, even = 102, r, t;
  for(int i = 0; i < 6; i++) {
    cin >> t;
    if ((0 == t % 2) && (t < even)) {
      even = t;
    }
    if ((0 != t % 2) && (t > odd)) {
      odd = t;
    }
  }
  r = odd - even;
  if (r > 0) {
    cout << r;
  }
  else {
    cout << -r;
  }
}
