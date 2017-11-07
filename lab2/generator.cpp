#include <bits/stdc++.h>

using namespace std;

void generate_and_print(int num_digits) {
  printf("%d", rand() % 9 + 1);
  for (int i = 1; i < num_digits; ++i) {
    printf("%d", rand() % 10);
  }
  printf("\n");
}

int main(int argc, char** argv) {
  if (argc < 2) {
    fprintf(stderr, "usage: %s <num_digits> [<seed>]\n", argv[0]);
    return 0;
  }

  int num_digits;
  sscanf(argv[1], "%d", &num_digits);

  int seed = clock();
  if (argc >= 3) {
    sscanf(argv[2], "%d", &seed);
  }

  srand(seed);
  fprintf(stderr, "Seed: %d\n", seed);

  generate_and_print(num_digits);
  generate_and_print(num_digits);

  return 0;
}
