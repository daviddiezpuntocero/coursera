#include<iostream>
using namespace std;

int main() {
  int numberOfData, data[100];

  cin >> numberOfData;

  for (int i = 0; i < numberOfData; i++) {
    cin >> data[i];
  }

  for (int i = numberOfData - 1; i >= 0; i--) {
    cout << data[i] << " ";
  }
}
