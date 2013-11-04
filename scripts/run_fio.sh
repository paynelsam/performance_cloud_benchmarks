#!/bin/bash

sudo aptitude update
sudo apt-get install -y fio

rm -rf fio_results
mkdir fio_results

FIO_CMD="fio --name fio_test_file --direct=1 --rw=randwrite --bs=16k \
          --size=1G --numjobs=16 --time_based --runtime=180 --group_reporting"

# Do a dry run to warm things up and make the data files
$FIO_CMD

for i in {0..5}
    do
        echo "working on iteration $i ============ "
        $FIO_CMD --output fio_results/fio-run-$i
    done