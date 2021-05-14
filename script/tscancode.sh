#bin/bash
cd ~/TScancode/TscanCode/release/linux/TscanCodeV2.14.24.linux/TscanCodeV2.14.2395.linux
echo 'tscancode安装目录为：'
pwd
./tscancode --xml --enable=all -q $1 > ~/$2/tscancode_`date +%Y%m%d%H%M`.xml 2>&1