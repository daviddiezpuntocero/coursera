#include<iostream>
using namespace std;

int main() {
  int n;
  int id[100];
  double rate[100];

  cin >> n;
  for (int i = 0; i < n; i++)
    {
      double initial, final;
      cin >> id[i] >> initial >> final;
      rate[i] = final / initial;
    }

  for (int i = 0; i < n - 1; i++)
    {
      for (int j = 0; j < n - i - 1; j++)
        {
          if (rate[j + 1] > rate[j]) {
            int tmp = id[j];
            id[j] = id[j + 1];
            id[j + 1] = tmp ;
            double tmp2 = rate[j];
            rate[j] = rate[j + 1];
            rate[j + 1] = tmp2;
          }
        }
    }
  double max = 0;
  int num1 = 0;
  for (int i = 0; i < n - 1; i++)
    {
      double diff = rate[i] - rate[i + 1];
      if (max < diff) {
        max = diff;
        num1 = i;
      }
    }

  cout << num1 + 1 << endl;
  for (int i = num1; i >= 0; i--)
    {
      cout << id[i] << endl;
    }
      
  cout << n - num1 - 1 << endl;
  for (int i = n - 1; i >= num1 + 1; i--)
    {
      cout << id[i] << endl;
    }
}
