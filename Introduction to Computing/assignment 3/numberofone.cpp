#include<iostream>
using namespace std;

int main() {
  
  int numberOfData, data[100], result[100];

  cin >> numberOfData;

  for(int i = 0; i < numberOfData; i++) {
    cin >> data[i];
    if (data[i] == 1) {
      result[i] = 1; 
      continue;
    } else if (data[i] == 0) {
      result[i] = 0;
      continue;
    } else {
      while(data[i] > 0) { 
        int a = data[i]/2;
        int b = data[i]%2;
        if (b == 1) {
          result[i] ++;
        }
        data[i] = a;
      }
    }
  } 
  
  for (int i = 0; i < numberOfData; i++) {
    cout << result[i] << endl;
  }
}
