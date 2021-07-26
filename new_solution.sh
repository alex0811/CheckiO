#!/bin/bash
# author:zhangfan
# CheckiO 打卡文档创建脚本

task_name=$1

if [ ${#task_name} == 0 ]
then
    echo "empty task name."
    exit
fi


time=$(date "+%Y-%m-%d")
task_folder_name=$task_name'-'$time
description_name=$task_name'-description.md'
solution_name=$task_name'-solution.py'

echo "创建 $task_name"
echo $task_folder_name
# 创建文件夹
mkdir $task_folder_name
# 创建描述文件
touch ./$task_folder_name/$description_name
# 创建问题对应的 python 文件
touch ./$task_folder_name/$solution_name