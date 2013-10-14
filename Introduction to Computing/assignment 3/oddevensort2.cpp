#include<iostream>
using namespace std;
int main() {
  //a[0..9]存储全部十个数
  int a[10];
  //i, j为循环变量
  int i = 0, j = 0;
  for (; i < 10; ++i) {
    cin >> a[i];
  }

  //对a整个冒泡排序
  for (i = 0; i < 10; ++i) {
    for (j = 0; j < 9 - i; j++) {
      if (a[j] > a[j + 1]) {
        if(a[j] > a[j + 1]) {
          int tmp = a[j + 1];
          a[j + 1] = a[j];
          a[j] = tmp;
        }
      }
    }
  }
  for (i = 0; i < 10; ++i) {
    if (a[i] % 2 == 1) {
      cout << a[i] << " ";
    }
  }
  for (i = 0; i < 10; ++i) {
    if (a[i] % 2 == 0) {
      cout << a[i] << " ";
    }
  }
  cout << endl;
  return 0;
}
