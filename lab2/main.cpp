#include <bits/stdc++.h>
#include <gmpxx.h>
#include <chrono>

#include "gcd.h"

using namespace std;
typedef mpz_class BigInt;

int main(int argc, char** argv) {
  if (argc < 2) {
    fprintf(stderr, "usage: %s <method>\n", argv[0]);
    fprintf(stderr, "method 1: Euclid's algorithm\n");
    fprintf(stderr, "method 2: binary GCD\n");
    fprintf(stderr, "method 3: factorization\n");
    fprintf(stderr,
            "the execution time is outputted to stderr and is in microseconds\n");
    return 0;
  }

  int method = -1;
  sscanf(argv[1], "%d", &method);
  unique_ptr<GCD> gcd = GCDFactory::get(method);
  if (gcd == nullptr) {
    fprintf(stderr, "Invalid method.\n");
    return 0;
  }

  BigInt a, b, c;
  cin >> a;
  cin >> b;
  long long start = chrono::duration_cast<chrono::microseconds>
                    (chrono::system_clock::now().time_since_epoch()).count();
  c = gcd->compute(a, b);
  cout << c << endl;
  long long stop = chrono::duration_cast<chrono::microseconds>
                   (chrono::system_clock::now().time_since_epoch()).count();
  cerr << stop - start << endl;

  return 0;
}
