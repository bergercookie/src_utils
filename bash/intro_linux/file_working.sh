#!/bin/bash

# Reading input
echo "Give me a directory name:"
read dir_name

mkdir $dir_name
cd $dir_name

pwd_ans=$PWD

echo "Hi I currently am in $pwd_ans"

touch file1 file2 file3 
echo kalimera > file1
echo kalinuxta > file2
echo ante gamisou >> file1

cat file1 file2 >file3

echo "Contents of file3 are the following:"
cat file3
