#!/bin/bash

basepath=$(cd `dirname $0`; pwd)

# screen
echo -e "$(cat ${basepath}/hello.md)"

# loading

# processbar <current> <total>  
processbar() {  
  local current=$1; local total=$2;  
  local maxlen=80; local barlen=60; local perclen=14;  
  local format="%-60s%20s"  
  local perc="][$current/$total]"  
  local progress=$((current*barlen/10))  
  local prog=$(printf '['; for i in `seq 0 $progress`; do printf 'h'; done)  
  printf "\r$format" $prog $perc  
}  
  
# Usage(Client)  
for i in `seq 1 10`; do  
  processbar $i 10  
  sleep 1  
done  
while true
do
  read temp
  if $temp;then
    break
  fi
done
echo ""  