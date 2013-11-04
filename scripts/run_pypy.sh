#!/bin/bash

sudo aptitude update
sudo apt-get install -y wget gcc make mercurial
sudo apt-get install -y \
gcc make python-dev libffi-dev libsqlite3-dev pkg-config \
libz-dev libbz2-dev libncurses-dev libexpat1-dev \
libssl-dev libgc-dev python-sphinx python-greenlet

rm -rf pypy
hg clone http://bitbucket.org/pypy/pypy pypy
( cd pypy
  hg up )

rm -rf ~/pypy_results
mkdir ~/pypy_results

for i in {1..6}
do
    (cd ~/pypy/pypy/goal/
        { time python ../../rpython/bin/rpython -Ojit targetpypystandalone; } >> ~/pypy_results/pypy-run-$i.out 2>&1
    )
done