# view cpu name
echo CPU: $(cat /proc/cpuinfo  | grep "model name" | head -1 | cut -d":" -f2)
echo Cores: $(cat /proc/cpuinfo | grep processor | wc -l)

# download kernel
cd /dev/shm
rm -r ./linux-3.*/
wget https://www.kernel.org/pub/linux/kernel/v3.x/linux-3.11.6.tar.xz
# extract
time tar -xpvf linux-3.11.6.tar.xz

# optional
mount -o remount,size=2G /run/shm/
mount -o remount,exec /dev/shm

# configure kernel
cd linux-3.*
make defconfig

# compile on 1 cpu
time make

cd ..
rm -r ./linux-3.*/
tar -xpvf linux-3.11.6.tar.xz
cd linux-3.*
make defconfig

# compile on all cups
time make -j$(cat /proc/cpuinfo | grep processor | wc -l)