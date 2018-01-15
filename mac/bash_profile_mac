export PATH="/usr/local/opt/openssl/bin:$PATH"
export JAVA_HOME=$(/usr/libexec/java_home)

# display  folders in cyan
export LSCOLORS="ga"

#colorize ls output
alias ls="ls -G"

#colorize prompt
#export PS1="\[\033[0;95m\][\u@\h]$ \[\033[0m\]"
export PS1="\[\033[0;95m\][rohan]\[\033[0m\]\[\033[0;94m\](\$(git branch 2>/dev/null | grep '^*' | colrm 1 2))\$\[\033[0m\] "

#safe move, copy and remove
alias mv="mv -i"
alias cp="cp -i"
alias rm="rm -i"
#alias postgres-start="pg_ctl -D /usr/local/var/postgres/ -l /usr/local/var/postgres/server.log start"
#alias postgres-stop="pg_ctl -D /usr/local/var/postgres/ -l /usr/local/var/postgres/server.log -m fast stop"

# unlimited .bash_history size
export HISTFILESIZE=
export HISTSIZE=

# export DISPLAY
export DISPLAY=$DISPLAY

# set the editor (will be also used for fc)
export VISUAL=vim
export EDITOR="$VISUAL"

# Export variable PYTHONSTARTUP to run code during python startup
export PYTHONSTARTUP="$HOME/.pythonrc"

# Export Git editor
export GIT_EDITOR=vim

# Postgres
alias pgstart="brew services start postgres"
alias pgstop="brew services stop postgres"

# Activate virtualenv
source ~/work/code/virtualenvs/base/bin/activate

# source the basrhc
source ~/.bashrc
