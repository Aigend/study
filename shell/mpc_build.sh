#!/usr/bin/sh

SCRIPT_PATH=$(
  cd $(dirname $0)
  pwd -P
)

PREFIX="[BUILD_MPC]"

echo "$PREFIX Script path: $SCRIPT_PATH"
echo "$PREFIX$# argument(s) $1 provided"

#--------------------------------------------
# change version file
awake_mpc_file="$SCRIPT_PATH/Upgrade/awake_mpc.sh"
mpc_upgrade_file="$SCRIPT_PATH/Upgrade/mpc_upgrade.sh"
save_mpc_version_file="$SCRIPT_PATH/Upgrade/save_mpc_version.sh"
global_file="$SCRIPT_PATH/WindowManager/src/Global.h"
android_manifest_file="$SCRIPT_PATH/WindowManager/android/AndroidManifest.xml"
echo "$PREFIX awake_mpc_file: $awake_mpc_file"
echo "$PREFIX mpc_upgrade_file: $mpc_upgrade_file"
echo "$PREFIX save_mpc_version_file: $save_mpc_version_file"
echo "$PREFIX global_file: $global_file"
echo "$PREFIX android_manifest_file: $android_manifest_file"

#--------------------------------------------
# detail version info
soft_name="fauna"
`git config --global --add safe.directory /home/build`
branch_tag=`git describe --abbrev=0 --tags`
modify_num=$1
if [ -z "$modify_num" ]; then
    modify_num="0"
fi
build_date=`date`
use_name=`whoami`
# machine=`dmidecode -t 1|grep UUID`
machine=""
target_palt="android 10 (android 10-android 11) arm_v7"
android_ndk=""
clang=""
#--------------------------------------------
#change version
current_version="023020.$branch_tag"
sed -i "s/023020.version/$current_version/g" $awake_mpc_file
sed -i "s/023020.version/$current_version/g" $mpc_upgrade_file
sed -i "s/023020.version/$current_version/g" $save_mpc_version_file
sed -i "s/023020.version/$current_version/g" $global_file
sed -i "s/android_version/$branch_tag/g" $android_manifest_file

detail_version="$soft_name version $branch_tag-$modify_num ($use_name@$machine) ($target_palt $android_ndk $clang) $build_date"
echo "$PREFIX detail_version: $detail_version"
sed -i "s/MPC_DETAIL_VERSION/$detail_version/g" $global_file
#--------------------------------------------
echo "**************buildMpc.sh**************"
cd ./WindowManager/protocol
echo "***environment is arm-android ,use tool /opt/android/3rdlibrary/protobuf/x86_64/bin/protoc***"
bash generateAll.sh arm-android
cd ../../
/opt/Qt/6.3.2/android_armv7/bin/qmake 
make -j8
make apk
