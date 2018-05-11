#!/bin/sh
#
# name     : Yet Another Windows 3.1
# author   : Inkblot Art Academy (dimpurr, volgorabgle, cyanlink)
# license  : MIT
#

# --- init ---

cmd=$(which tmux)      # tmux path
session=$(hostname -s) # session name
basepath=$(cd `dirname $0`; pwd)

# check tmux install & set conf

if [ -z $cmd ]; then
	echo "You need to install tmux."
	exit 1
fi
echo "Symlinking _tmux.conf to $HOME/.tmux.conf"
ln -sf $basepath/_tmux.conf $HOME/.tmux.conf

# --- run ---

$cmd has -t $session 2> /dev/null

if [ $? != 0 ]; then

	# - hello

	$cmd new -d -n hello -s $session "zsh ${basepath}/main/hello.sh; ${cmd} selectp -t ${session}:main.2"
	# -d detach other clients
	# -s session name
	# -n window name
	# sleep 1s
	# $cmd splitw -v -p 20 -t $session "pry" # debug
	# $cmd neww -n cmus -t $session "cmus"

	# - main
	$cmd neww -n main -t $session "zsh ${basepath}/main/main.sh"
	
	# - header
	$cmd splitw -b -v -l 2 -t $session "zsh ${basepath}/header/header.sh"

	# - footer
	$cmd selectp -t $session:main.2
	$cmd splitw -v -l 1 -t $session "echo 'footer'; read -1"

	# - main right
	$cmd selectp -t $session:main.2
	$cmd splitw -h -l 5 -t $session "zsh ${basepath}/sidebar/sidebar.sh"
	# -l size
	# -p percentage
	# -h horizontal split
	# -v vertical split
	# $cmd resizep -y 99 -t $session:main.2

	# fin
	$cmd selectw -t $session:hello
fi

$cmd att -t $session

exit 0