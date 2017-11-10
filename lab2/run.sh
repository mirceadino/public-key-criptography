#!/bin/bash

make generator
make main

timeout=1

for i in 2 4 8 16 32 64 128 256 512 1024; do
  ./generator "$i" > tmp 2> /dev/null
  echo "Numbers of $i digits"
  cat tmp
  echo "GCD"
  ./main 1 < tmp 2> /dev/null
  echo "Results"
  gtimeout "$timeout" ./main 1 < tmp > /dev/null
  gtimeout "$timeout" ./main 2 < tmp > /dev/null
  # gtimeout "$timeout" ./main 3 < tmp > /dev/null
  gtimeout "$timeout" ./main 4 < tmp > /dev/null
  echo "---"
done;

make clean
rm tmp
