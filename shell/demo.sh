#!/usr/bin/sh
#--------------------------------------------
# author:wenlong.jin
# date: 2023.3.2
#--------------------------------------------
##### 用户配置区 开始 #####
#
##### 用户配置区 结束 #####
:echo "**************net.sh 调试配置docker使用**************"
if [ -f /etc/docker/daemon.json ];then 
echo "open docker net "
mv /etc/docker/daemon.json /etc/docker/bak
elif [ -f /etc/docker/bak ];then 
echo "close docker net "
mv /etc/docker/bak /etc/docker/daemon.json
fi
echo "stop docker"
service docker stop
echo `ps aux | grep docker`
echo "start docker"
service docker start
echo `ps aux | grep docker`

array_name=(
value0
value1
value2
value3
)

valuen=${array_name[n]}
# 使用 @ 符号可以获取数组中的所有元素
echo ${array_name[@]}

# 取得数组元素的个数
length=${#array_name[@]}
# 或者
length=${#array_name[*]}
# 取得数组单个元素的长度
lengthn=${#array_name[n]}

string="runoob is a great site"
# 查找字符 i 或 o 的位置(哪个字母先出现就计算哪个)
echo `expr index "$string" io` # 输出 4

echo "执行的文件名：$0";
echo "QT 版本：$1";
echo "NDK 版本：$2";
echo "Python 版本：$3";
for file in `ls /etc`;do
echo $file
done

test=$(env | grep USER | cut -d "=" -f 2)

if [ "$test"==root ]
then 
echo "current user is root"
fi


#git clone git@github.com:pyenv/pyenv.git ./context/.pyenv

#wget https://repo.huaweicloud.com/java/jdk/11.0.2+9/jdk-11.0.2_linux-x64_bin.tar.gz -P 

#docker run -it --rm -v /home/zoo/opt:/opt -v /home/zoo/nfs:/nfs --name root mpc:root /bin/bash

echo '输入 1 到 4 之间的数字:'
echo '你输入的数字为:'
read aNum
case $aNum in
1) echo '你选择了 1'
;;
2) echo '你选择了 2'
;;
3) echo '你选择了 3'
;;
4) echo '你选择了 4'
;;
*) echo '你没有输入 1 到 4 之间的数字'
;;
esac

site="runoob"

case "$site" in
"runoob") echo "菜鸟教程"
;;
"google") echo "Google 搜索"
;;
"taobao") echo "淘宝网"
;;
esac

while:
do
echo -n "输入 1 到 5 之间的数字:"
read aNum
case $aNum in
1|2|3|4|5) echo "你输入的数字为 $aNum!"
;;
*) echo "你输入的数字不是 1 到 5 之间的! 游戏结束"
#continue
#echo "游戏结束"
break
;;
esac
done

EOF

echo "**************cicdIcc.sh**************"
if [ -d "${HOME}/mpc-main" ];then
sudo rm -rf ${HOME}/023029
fi
echo "####Step1:git clone code####"
git clone -b develop --recurse-submodules git@git.nevint.com:PERD/PowerSwap/powerswap_3.0/023029.git ${HOME}/023029/
echo "####Step2:bash sh and qmake and make under network none####"
sudo docker run -it --rm --network none -v ${HOME}/023029:/tmp/023029 --name buildIcc hrb.nioint.com/ps-cicd/mpc:latest /bin/bash buildIcc.sh

#cd /tmp/mpc-main
ROOT_DIR=$(pwd)
#cd ./WindowManager/protocol
BUILD_ENV=$1
if [ "$BUILD_ENV" == "arm-android" ]; then
echo "***environment is arm-android ,use tool /opt/android/3rdlibrary/protobuf/x86_64/bin/protoc***"
bash ${ROOT_DIR}/WindowManager/protocol/generateAll.sh $BUILD_ENV
#cd $ROOT_DIR
/opt/Qt/6.3.2/android_armv7/bin/qmake CONFIG+=debug CONFIG+=qml_debug
make
make apk
MPC_VERSION=`cat Upgrade/mpc_upgrade.sh | grep -oP "023020\.\d+\.\d+\.\d+\.apk" | grep -oP '(\d+\.\d+\.\d+)\.apk' | grep -oP '\d+\.\d+\.\d+'`
mkdir $MPC_VERSION
cd $MPC_VERSION
echo $MPC_VERSION > version.txt
cp WindowManager/android-build/build/outputs/apk/debug/android-build-debug.apk 023020.${MPC_VERSION}.apk
cp Upgrade/mpc_upgrade.sh mpc_upgrade.sh
zip ../023020.${MPC_VERSION}.zip version.txt mpc_upgrade.sh 023020.${MPC_VERSION}.apk
cd ../
elif [ "$BUILD_ENV" == "x86" ]; then
echo "environment is x86 , use tool default"
exit 1
else
echo -e "\033[31merror:please set build environment.[arm-android/x86]\033[0m"
exit 1
fi
