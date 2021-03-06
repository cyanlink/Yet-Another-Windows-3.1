```
█╗   ██╗ █████╗  ██╗    ██╗
╚██╗ ██╔╝██╔══██╗██║    ██║
 ╚████╔╝ ███████║██║ █╗ ██║
  ╚██╔╝  ██╔══██║██║███╗██║   'Yet Another Windows 3.1' v0.1
   ██║   ██║  ██║╚███╔███╔╝   (c) Inkblot Art Academy
   ╚═╝   ╚═╝  ╚═╝ ╚══╝╚══╝    (dimpurr, volgorabgle, cyanlink)
```
this is a read me of shell-practice

# User

### Dependencies

* software
	* tmux
	* vim
	* emacs
	* ncdu
* env
	* python
	* go

# Dev

* UI
	* tmux
	* ncurses
* Components
	* neofetch (hello)
	* ncdu (file)
	* curls (weather)
	* emacs (game)
	* cmus + musicbox + cava (music)

## CMD

* `wego -frontend emoji -l 39.961,116.350 -forecast-api-key 0656b207df72ebf3ed8f597c258ed731 -d 2`

## Note

### Dimpurr

#### Linux tricks

* http://blog.jobbole.com/41129/
* https://www.csdn.net/article/1970-01-01/2807272

#### Useful commands

```bash
cd /Users/dimpurr/Workflow/00Programing/Shell/shell-practice

ln -sf /Users/dimpurr/Workflow/00Programing/Shell/shell-practice/_tmux.conf /Users/dimpurr/.tmux.conf
```

#### 常用 TMUX 操作

前缀按键： `Ctrl + A`

* `d` 退出整个 TMUX
* `&` 退出当前 Window
* `q` 退出当前 Pane
* `s` 窗口管理器

## Refer

### Curses & Ncurses

* https://docs.python.org/3/library/curses.html#

### TMUX

* http://man.openbsd.org/OpenBSD-current/man1/tmux.1

```bash
new-session [-AdDEP] [-c start-directory] [-F format] [-n window-name] [-s session-name] [-t group-name] [-x width] [-y height] [shell-command]
(alias: new)


```

* https://blog.csdn.net/robertbaker/article/details/42172203
* https://github.com/xuxiaodong/tmuxen

```markdown
tmux的任何指令，都包含一个前缀，也就是说，你按了前缀(一组按键，默认是Ctrl+b)以后，系统才知道你接下来的指令是发送给tmux的。

C-b ? 显示快捷键帮助
C-b C-o 调换窗口位置，类似与vim 里的C-w
C-b 空格键 采用下一个内置布局
C-b ! 把当前窗口变为新窗口
C-b " 模向分隔窗口
C-b % 纵向分隔窗口
C-b q 显示分隔窗口的编号
C-b o 跳到下一个分隔窗口
C-b 上下键 上一个及下一个分隔窗口
C-b C-方向键 调整分隔窗口大小
C-b c 创建新窗口
C-b 0~9 选择几号窗口
C-b c 创建新窗口
C-b n 选择下一个窗口
C-b l 切换到最后使用的窗口
C-b p 选择前一个窗口
C-b w 以菜单方式显示及选择窗口
C-b t 显示时钟
C-b ; 切换到最后一个使用的面板
C-b x 关闭面板
C-b & 关闭窗口
C-b s 以菜单方式显示和选择会话
C-b d 退出tumx，并保存当前会话，这时，tmux仍在后台运行，可以通过tmux attach进入 到指定的会话
```

### VolgoRabgle


* https://linux.cn/article-6423-1.html

ledger:

An accounting system accessed from command-line.
Creat a file end with '.dat' , use ledger to operte.

command:
ledger -f filename.dat balance
ledger -f filename.dat register tags

.dat file reference:
2018/5/17 Volgo
    Expenses:Gas       $10.00
    Liabilities:Fix    $-10.00

ref: https://www.ledger-cli.org/

Taskwarrior:

A todo-list system accessed from command-line.
Yet not find how does it works, but it doesn't matter.

ref: https://taskwarrior.org/docs/commands/
ref: https://taskwarrior.org/download/

commmad useful:
[start with 'task']
add            Add a new task
annotate       Add annotate to a task
count          Count total number of all task [use "status:pending count" to count current task
done           Finish a task
list           List the task list
start          Mark a task is being dealt
stop           Stop the Mark