#!/bin/zsh
basepath=$(cd `dirname $0`; pwd)

echo "Loading MUSICD player ..."
sleep 2s
python ${basepath}/musicd/musicd.py
read -n 1