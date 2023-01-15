##  Vim 在 bash 中的显示与 tmux 中的显示不同

解决方法如下:
* 在~/.bashrc 中添加alias tmux='tmux -2',然后使配置生效$source ~/.bashrc.
* 在~/.tmux.conf 中添加 set -g default-terminal "screen-256color"


