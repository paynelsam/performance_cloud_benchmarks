#!/bin/bash

sudo aptitude update
sudo apt-get install -y wget gcc make iozone3

rm -rf iozone_results
mkdir iozone_results

for i in {1..6}
do
    iozone -Ra -g 2G -b iozone_results/iozone-run-$i.csv > iozone_results/iozone-run-$i.out
done