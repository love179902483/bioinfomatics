
## tmux 的几个名词

> session, window, pane 在这里我们就把他们分别叫做会话，窗口，窗格子。


通常我们在终端中操作一个任务的时候，一旦终端关闭，任务也就结束了，被强制关闭了，在 tmux 中 使用 session 就可以解决这个问题，我们可以把当前操作的任务隐藏起来，在视觉上让它消失，任务继续执行着，当我们想返回任务做一些操作的时候，它可以很方便的回来，我们通常把上面的操作就做 session 操作，我们可以把 session 给隐藏起来，我们也可以把 session 给真的关掉。


在tmux中有一个窗口的概念：
	当前呈现在我们面前的这一个区域就是一个窗口(当前的终端界面),窗口可以被不断切割，切割成一个个小块，这一个个小块我们叫做窗格子(pane)，这就是窗口和窗格的概念。


#### *总结*： 一个session通常指的是一个任务里面可有很多个窗口，一个窗口又可以有很多个窗格。


## tmux前缀健

如果想使用tmux的快捷键，我们必须使用tmux的前缀键 ctrl + b, 在tmux中所有的快捷键都需要通过前缀键来唤醒的。

如果 ctrl + b的前缀键感觉不是很友好，可以通过tmux配置文件.tmux.conf进行修改。

## 新建 session

` tmux new -s <session-name>`

例如：新建一个名称是 test 的session： tmux new -s test

## 离开 session

有时候我们需要离开终端，操作其他任务，需要离开该任务，但邮想该任务在后台执行，这时候我们需要在tmux的任何一个窗格中输入如下命令：

` tmux detach `

也可以使用快捷键 ctrl + b d，这里解释一下该快捷键，tmux离开session的快捷键是d，但是在tmux当中任何快捷键都需要搭配tmux的前缀见ctrl + b来唤醒。

## 查看session列表

有时候，我们需要同时操作几个session,我们可以通过如下命令来查看我们目前操作了几个session：
`tmux ls`

也可以通过快捷键 ctrl + b s列出所有的session


## 进入session

`tmux attach -t <session-name>`

`tmux a -t <session-name>`

其中a是attach的简写形式

## 关闭session 
`tmux kill-session -t <session-name>`
`tmux kill-session-t test`

也可以使用 ctrl + d来关闭当前的session


## 切换sessionn
`tmux switch -t <session-name>`

## 重命名 session

`tmux rename-session -t <old—session-name> <new-session-name>`

`tmux rename-session -t old new`

也可以通过使用 ctrl + b $ 来重新命名当前的session

## 切割窗口

	* 上下切割 `tmux split-window`
	* 左右切割 `tmux split-window -h`
	* 左右切割快捷键 ctrl + b %
	* 上下切割快捷键 ctrl + b "

## 不同窗口移动光标

`tmux select-pane -U`

## 把当前光标移动到上方窗格
`tmux select-pane -D`

## 把当前光标移动到下方窗格
`tmux select-pane -L`
## 把当前光标移动到左边窗格
`tmux select-pane -R`

## 移动窗格光标的快捷键

	* ctrl + b <arrowkey> 例如：ctrl + b 方向键上。把光标移动到了上方的窗格
	* ctrl + b ; 光标切换到了上一个窗格
	* ctrl + b o 光标切换到了下一个窗格

## 交换窗格的位置

`tmux swap-pane -U`

## 当前窗格上移动
`tmux swap-apne -D`
