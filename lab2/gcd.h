#include <bits/stdc++.h>
#include <gmpxx.h>

typedef mpz_class BigInt;

class GCD {
  public:
    GCD() {}
    virtual ~GCD() {}
    virtual BigInt compute(BigInt a, BigInt b) = 0;
};


class EuclidGCD: public GCD {
  public:
    BigInt compute(BigInt a, BigInt b);
};


class SubstractionGCD: public GCD {
  public:
    BigInt compute(BigInt a, BigInt b);
};



class BinaryGCD: public GCD {
  public:
    BigInt compute(BigInt a, BigInt b);
};


class FactorizationGCD: public GCD {
  public:
    BigInt compute(BigInt a, BigInt b);
};


class GCDFactory {
  public:
    static std::unique_ptr<GCD> get(int method) {
      if (method == 1) {
        return std::make_unique<EuclidGCD>();
      } else if (method == 2) {
        return std::make_unique<SubstractionGCD>();
      } else if (method == 3) {
        return std::make_unique<BinaryGCD>();
      } else if (method == 4) {
        return std::make_unique<FactorizationGCD>();
      }
      return nullptr;
    }
};

BigInt EuclidGCD::compute(BigInt a, BigInt b) {
  BigInt r;
  while (b != 0) {
    r = a % b;
    a = b;
    b = r;
  }
  return a;
}

BigInt SubstractionGCD::compute(BigInt a, BigInt b) {
  while (a != b) {
    if (a > b) {
      a -= b;
    } else {
      b -= a;
    }
  }
  return a;
}

BigInt BinaryGCD::compute(BigInt a, BigInt b) {
  if (a == 0) {
    return b;
  }
  if (b == 0) {
    return a;
  }

  BigInt gcd = 1;
  while (a % 2 == 0 && b % 2 == 0) {
    gcd *= 2;
    a /= 2;
    b /= 2;
  }
  while (a != b) {
    while (a % 2 == 0) {
      a /= 2;
    }
    while (b % 2 == 0) {
      b /= 2;
    }
    if (a > b) {
      a -= b;
    } else if (b > a) {
      b -= a;
    }
  }
  return a * gcd;
}

BigInt FactorizationGCD::compute(BigInt a, BigInt b) {
  if (a == 0) {
    return b;
  }
  if (b == 0) {
    return a;
  }

  BigInt gcd = 1;
  int e = 0, f = 0;
  while (a % 2 == 0) {
    ++e;
    a /= 2;
  }
  while (b % 2 == 0) {
    ++f;
    b /= 2;
  }
  for (int i = 0; i < std::min(e, f); ++i) {
    gcd *= 2;
  }

  for (BigInt p = 3; a != 1 && b != 1; p += 2) {
    int e = 0, f = 0;
    while (a % p == 0) {
      ++e;
      a /= p;
    }
    while (b % p == 0) {
      ++f;
      b /= p;
    }
    for (int i = 0; i < std::min(e, f); ++i) {
      gcd *= p;
    }
  }

  return gcd;
}
