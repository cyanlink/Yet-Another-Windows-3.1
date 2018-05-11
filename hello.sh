#!/bin/bash

basepath=$(cd `dirname $0`; pwd)

# screen
cat ${basepath}/hello.md

# loading

# processbar <current> <total>  
processbar() {  
  local current=$1; local total=$2;  
  local maxlen=80; local barlen=66; local perclen=14;  
  local format="%-${barlen}s%$((maxlen-barlen))s"  
  local perc="[$current/$total]"  
  local progress=$((current*barlen/total))  
  local prog=$(printf '['; for i in `seq 0 $progress`; do printf '★'; done)  
  printf "\r$format" $prog $perc  
}  
  
# Usage(Client)  
for i in `seq 1 10`; do  
  processbar $i 10  
  sleep 1  
done  
echo ""  