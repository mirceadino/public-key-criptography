#include <bits/stdc++.h>

using namespace std;

// Computes gcd of two numbers.
int gcd(int a, int b) {
  if (a == 0) {
    return b;
  }
  if (b == 0) {
    return a;
  }
  return gcd(b, a % b);
}

// Computes exponentiation of a to the power of n modulo mod.
int exp(int a, int n, int mod) {
  if (n == 0) {
    return 1;
  }
  if (n == 1) {
    return a;
  }
  long long t = exp(a, n / 2, mod);
  return (t * t) % mod * exp(a, n % 2, mod) % mod;
}

// Computes Euler's totient function for a number i.e. the number of comprimes
// that are below n.
int phi(int n) {
  int phi = 0;
  for (int i = 1; i < n; ++i) {
    if (gcd(n, i) == 1) {
      ++phi;
    }
  }
  return phi;
}

// Computes the modular inverse of a modulo mod.
int inv(int a, int mod) {
  if (gcd(a, mod) != 1) {
    return -1;
  }
  return exp(a, phi(mod) - 1, mod);
}

int main() {
  int a, b, n;
  printf("Solving: a * x = b (mod n)\n");
  printf("Read a, b, n: ");
  cin >> a >> b >> n;
  printf("%d * x = %d (mod %d)\n", a, b, n);

  int x;
  int d = gcd(a, n);
  if (d == 1) {
    x = inv(a, n) * 1LL * b % n;
    printf("Solution: x = %d.\n", x);
  } else if (b % d == 0) {
    x = inv(a / d, n / d) * 1LL * (b / d) % (n / d);
    printf("Solution: x = %d.\n", x);
  } else {
    printf("No solution.\n");
  }

  return 0;
}
