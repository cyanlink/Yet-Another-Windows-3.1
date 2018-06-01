#!/bin/sh
basepath=$(cd `dirname $0`; pwd)

wegocmd="/Users/dimpurr/Workflow/00Programing/Go/bin/wego"
# w3m google.co.jp
# ncdu $basepath/playground
# ncdu $basepath/../../..
# zsh
# read -n 1

#!/bin/bash
# using select in the menu

cowsay -f dragon " Welcome You ! "

PS3="Do you want: "
select option in "[Control] Shell" "[Control] File" "[Control] Mission" "[Online] Internet" "[Online] BYRBBS" "[Net] Weather" "[Net] Netease Music" "[Play] Movie: Star War" "[Play] Game" "[Play] sl Train"
do
 case $option in
 "[Control] Shell")
 zsh ;;
 "[Control] File")
 ncdu $basepath/../../.. ;;
 "[Online] Internet")
 w3m google.com ;;
 "[Online] BYRBBS")
 luit -encoding gbk telnet bbs.byr.cn ;;
 "[Control] Mission")
 htop ;;
 "[Play] Game")
 emacs $basepath/emacs.md ;;
 "[Play] sl Train")
 sl ;;
 "[Net] Weather")
 $wegocmd -frontend emoji -l 39.961,116.350 -forecast-api-key 0656b207df72ebf3ed8f597c258ed731 -d 2 ;;
 "[Net] Netease Music")
 musicbox ;;
 "[Play] Movie: Star War")
 telnet towel.blinkenlights.nl ;;
 *)
 echo "Sorry, wrong selection";;
 esac
done
clear