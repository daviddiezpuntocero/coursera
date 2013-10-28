#include<iostream>
using namespace std;

int main() {
  int n, h = -1, t;
  cin >> n;
  for(int i = 0; i < n; i++) {
    cin >> t;
    if(t > h) {
      h = t;
    }
  }
  cout << h;
}
