#!/bin/sh
#
# name     : Yet Another Windows 3.1
# author   : Inkblot Art Academy (dimpurr, volgorabgle, cyanlink)
# license  : MIT
#

cmd=$(which tmux)      # tmux path
session=$(hostname -s) # session name

if [ -z $cmd ]; then
    echo "You need to install tmux."
    exit 1
fi

$cmd has -t $session 2> /dev/null

if [ $? -ne 0 ]; then
    $cmd new -d -n irc -s $session "irssi"
    $cmd neww -n zsh -t $session "zsh"
    $cmd selectw -t $session:2
fi

$cmd att -t $session

exit 0