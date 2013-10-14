#include<iostream>
using namespace std;

int main() {
  //定义变量
  //all为全部十个数;odd纪录奇数，even纪录偶数，odd，even最多10个
  const int MAX_NUMBER = 10;
  int all[MAX_NUMBER], odd[MAX_NUMBER], even[MAX_NUMBER];
  //i, j为循环变量
  int i = 0, j = 0;
  //依次输入十个数至all，i为all的下标
  for (; i < MAX_NUMBER ; i++) {
    cin >> all[i];
  }

  //numOdd, numEven分别纪录奇数，偶数的个数
  int numOdd = 0, numEven = 0;

  //遍历数组all，如果当前all[i]为奇数则放入odd[numOdd], 偶数放入even[numEven]
  for (i = 0; i < MAX_NUMBER; ++i) {
    if (all[i] % 2 != 0) {
      odd[numOdd] = all[i];
      numOdd ++;
    } else {
      even[numEven] = all[i];
      numEven ++;
    }
  }

  //对odd冒泡排序
  for (i = 0; i < numOdd; ++i) {
    for (j = 0; j < numOdd - i - 1; j++) {
      if (odd[j] > odd[j + 1]){
        int tmp = odd[j];
        odd[j] = odd[j+1];
        odd[j + 1] = tmp;
      }
    }
  }

  //对even冒泡排序
  for (i = 0; i < numEven; ++i) {
    for (j = 0; j < numEven - 1 - i; j++) {
      if (even[j] > even[j + 1]){
        int tmp = even[j];
        even[j] = even[j + 1];
        even[j + 1] = tmp;
      }
    }
  }

  for(i = 0; i < numOdd; i++) {
    cout << odd[i] << " ";
  }

  for(i = 0; i < numEven; i++) {
    cout << even[i] << " ";
  }

  cout << endl;
  return 0;
}
