#!/bin/bash

basepath=$(cd `dirname $0`; pwd)

# screen
cat ${basepath}/hello.md

# loading

echo ""
echo ""
echo ""
echo ""
echo "       Now Loading ..."

start="       [ "
end=" ]"
for i in $(seq 1 10)  
do
	prog=""

	for ii in $(seq 1 $i)
	do
		prog="${prog}████"
	done

	prog="${prog}"

	if [ $i != "10" ]; then
		let ip=$i+1
		for iii in $(seq $ip 10)
		do
			prog="${prog}    "
		done
	fi

	fin="${start}${prog}${end}"
	echo -en "$fin $i\r"
	sleep 0.05s
done
echo ""
echo ""
echo "                         [Enter]"
read -n 1