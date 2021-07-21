#!/bin/bash
# author:zhangfan
# CheckIO 打卡文档创建脚本

task_name=$1
time=$(date "+%Y-%m-%d")
task_folder_name=$task_name'-'$time

echo "创建 $task_name"
echo $task_folder_name
# 创建文件夹
mkdir $task_folder_name
# 创建描述文件
touch ./$task_folder_name/description.md
# 创建问题对应的 python 文件
touch ./$task_folder_name/solution.md