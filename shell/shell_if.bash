#!/bin/bash
# chmod +x ./test.sh  #使脚本具有执行权限
# 直接写 test.sh，linux 系统会去 PATH 里寻找有没有叫 test.sh 的，而只有 /bin, /sbin, /usr/bin，/usr/sbin 等在 PATH 里
# ./test.sh  #执行脚本

# /bin/sh test.sh
echo "Hello World !"
num1=$[2*3]
num2=$[1+5]
if test $[num1] -eq $[num2]
then
    echo '两个数字相等!'
else
    echo '两个数字不相等!'
fi

# 注意，第二次赋值的时候不能写$your_name="alibaba"，使用变量的时候才加美元符（$
# 变量名后面的等号左右不能有空格
your_name="tom"
echo $your_name
your_name="alibaba"
echo $your_name

myUrl="https://www.google.com"
readonly myUrl
# myUrl="https://www.runoob.com"

myUrl="https://www.runoob.com"
unset myUrl
echo $myUrl

your_name="runoob"
str="Hello, I know you are \"$your_name\"! \n"
echo -e $str

your_name="runoob"
# 使用双引号拼接
greeting="hello, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo $greeting  $greeting_1

# 使用单引号拼接
greeting_2='hello, '$your_name' !'
greeting_3='hello, ${your_name} !'
echo $greeting_2  $greeting_3

# array_name=(
# value0
# value1
# value2
# value3
# )

:<<EOF

# 取得数组元素的个数
length=${#array_name[@]}
# 或者
length=${#array_name[*]}
# 取得数组单个元素的长度
lengthn=${#array_name[n]}
EOF

:<<'
注释内容...
注释内容...
注释内容...
'
# 这里可以添加脚本描述信息

:<<!
注释内容...
注释内容...
注释内容...
array_name[0]=value0
array_name[1]=value1
array_name[n]=valuen
${数组名[下标]}
valuen=${array_name[n]}
使用 @ 符号可以获取数组中的所有元素
echo ${array_name[@]}
!


echo "Shell 传递参数实例！";
echo "执行的文件名：$0";
echo "第一个参数为：$1";
echo "第二个参数为：$2";
echo "第三个参数为：$3";

echo "Shell 传递参数实例！";
echo "第一个参数为：$1";
echo "参数个数为：$#";
echo "传递的参数作为一个字符串显示：$*";

echo "-- \$* 演示 ---"
for i in "$*"; do
    echo $i
done

echo "-- \$@ 演示 ---"
for i in "$@"; do
    echo $i
done

# 数组中可以存放多个值。Bash Shell 只支持一维数组（不支持多维数组），初始化时不需要定义数组大小

a=10
b=20
# 原生bash不支持简单的数学运算，但是可以通过其他命令来实现，例如 awk 和 expr，expr 最常用
# 表达式和运算符之间要有空格，例如 2+2 是不对的，必须写成 2 + 2
val=`expr $a + $b`
echo "a + b : $val"

val=`expr $a - $b`
echo "a - b : $val"

val=`expr $a \* $b`
echo "a * b : $val"

val=`expr $b / $a`
echo "b / a : $val"

val=`expr $b % $a`
echo "b % a : $val"

# 条件表达式要放在方括号之间，并且要有空格，例如: [$a==$b] 是错误的，必须写成 [ $a == $b ]
if [ $a == $b ]
then
   echo "a 等于 b"
fi
if [ $a != $b ]
then
   echo "a 不等于 b"
fi



echo “按月选择季度”
read -p "请输入数字(1-12):num=" num
case $num in
   1|2|3)
   echo "第一季度"
   ;;
   4|5|6)
   echo "第二季度"
   ;;
   7|8|9)
   echo "第三季度"
   ;;
   10|11|12)
   echo "第四季度"
   ;;
   *)
   echo "输入错误，注输入的数字必须在1-12之间"
   ;;
esac



for i in 1 2 3 4;do echo "The num is $i";done;

for i in 1 2 3 4
do
   echo "the num is $i"
   echo "the num is $i"
done


sum=0
for((i=0;i<=100;i++))
do
    sum=$[ $sum + $i]
done
echo "1-100的和为：total=$sum"


i=10
echo "10秒倒计时开始"
while(( $i<=0 ))
do 
    echo $i
    let "i--"
done
echo "10秒倒计时结束"


i=0
while :
do
   echo "无限叠加$(i++)"
done


i=10
echo "10秒倒计时开始"
until(( $i<0 ))
do
    echo $i
    let "i--"
done
echo "10秒倒计时结束"