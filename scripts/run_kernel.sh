#!/bin/bash

# install apps
apt-get update -qq
apt-get install -y gcc make libc6-dev bzip2 bc --no-install-recommends
apt-get install -y fakeroot build-essential crash kexec-tools makedumpfile kernel-wedge

rm -rf kernel_results
mkdir ~/kernel_results

for i in {1..6}
do
    ./kernel.sh >> ~/kernel_results/result-$i.out 2>&1
done
