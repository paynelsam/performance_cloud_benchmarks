#!/bin/bash

sudo aptitude update
sudo apt-get install -y wget gcc make

wget https://byte-unixbench.googlecode.com/files/UnixBench5.1.3.tgz
tar -xzf UnixBench5.1.3.tgz
cd UnixBench
rm -rf ../unixbench_results
mkdir ../unixbench_results

for i in {1..6}
do
    ./Run
    mv results ../unixbench_results/results-run$i
    mkdir results
done