#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export HISTCONTROL=ignoreboth:erasedups

#PS1='[\u@\h \W]\$ '
#PS1='\e[31m\u\e[39m@\h [\e[35m\W\e[39m]\n\e[34m» \e[39m'
PS1='\e[31m\u\e[39m@\h [\e[35m\W\e[39m]\n\e[34m» \e[39m'
#PS1='\n\e[31m>> \e[39m '
#PS1='\e[31m>> \e[39m'
#PS1='\e[31m \e[39m\e[30m \e[39m'

#list
alias ls='ls --color=auto'
alias la='ls -a'
alias ll='ls -la'
alias l='ls' 					
alias l.="ls -A | egrep '^\.'"      

#fix obvious typo's
alias cd..='cd ..'
alias sl="ls"
alias pdw="pwd"

## Colorize the grep command output for ease of use (good for log files)##
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

#readable output
alias df='df -h'

alias merge="xrdb -merge ~/.Xresources"

# Aliases for software managment
# pacman or pm
alias pmsyu="sudo pacman -Syu --color=auto"
alias pacman='sudo pacman --color auto'
alias update='sudo pacman -Syu'
# pacaur or pc
alias pcsyu="pacaur -Syu"
# packer or pk
alias pks="packer -S"
alias pksn="packer -S --noconfirm --noedit"
alias pksyu="packer -Syu  --noconfirm --noedit"

alias fixpng="find . -type f -name "*.png" -exec convert {} -strip {} \;"

## ls group directory first
alias lsf="ls --group-directories-first"

## A funny meme :D
##
alias love="echo 'Shell: Love not found' | lolcat"
alias happines="echo 'Shell: Happines not found' | lolcat"
alias peace="echo 'Shell: Peace not found' | lolcat"
alias kill="echo 'Shell: You need to specify whom to kill' | lolcat"
alias kill-everyone="echo 'Shell: But! Genocide is illegal Sir!!' | lolcat"
#alias love="echo '\e[31mShell: \e[34mLove not found \uF08A \uF00D' && echo ' '"
#alias happines="echo '\e[31mShell: \e[33mHappines not found \uF119' && echo ' '"
#alias peace="echo '\e[31mShell: \e[35mPeace not found \uF0E3' && echo ' '"
#alias kill="echo '\e[32mShell: \e[31mYou need to specify whom to kill \uF05B' && echo ' '"
#alias kill-everyone="echo '\e[32mShell: \e[31mBut! Genocide is illegal Sir!! \uF05C' && echo ' '"

## Start CAVA Visualizer with color config
##
alias cava-froly="cava -p ~/.config/cava/config-froly"
alias cava-crimson="cava -p ~/.config/cava/config-crimson"
alias cava-cyan="cava -p ~/.config/cava/config-cyan"
alias cava-blue="cava -p ~/.config/cava/config-blue"

## Neofetch for Urxvt with internal padding
alias neopad="neofetch --config /home/addy/.config/neofetch/config-padding"

## Neofetch with different distro logo color
##
alias neofetch-blue="neofetch --source .neofetch/al-blue.png --colors 4 4 4 4 4"
alias neofetch-crimson="neofetch --source .neofetch/al-crimson.png --colors 1 1 1 1 1"
alias neofetch-froly="neofetch --source .neofetch/al-froly.png --colors 9 9 9 9 9"
alias neofetch-lavender="neofetch --source .neofetch/al-lavender.png --colors 13 13 13 13 13"
alias neofetch-lime="neofetch --source .neofetch/al-lime.png --colors 2 2 2 2 2"
alias neofetch-orange="neofetch --source .neofetch/al-orange.png --colors 3 3 3 3 3"
alias neofetch-paper="neofetch --source .neofetch/al-paper.png --colors 7 7 7 7 7"
alias neofetch-violet="neofetch --source .neofetch/al-violet.png --colors 5 5 5 5 5"

## View and set wallpaper with feh
alias feh-view="feh --scale-down --auto-zoom"
alias feh-set="feh --bg-fill"
#alias feh-set="echo 'Wallpaper has been set for You, very nice choice :)' && feh --bg-fill"

## Refresh font cache
alias font-refresh="fc-cache -fv"

## ncmpcpp with album-art
alias ncmpcpp-art="ncmpcpp -c .ncmpcpp/config-art"

## self-destruct
rm()
{
  if [ "$1" = "-rf/" ]
  then
    shift
    echo '' && echo 'Do a self destruct in 5.. 4.. 3.. 2.. 1..' && echo 'Just kidding :p' && echo '' && echo "Let's taking a screenshot instead" && scrot -cd 5 "$@"
  else
    command rm "$@"
  fi
}

## termite light
alias termite-light="termite -c ~/.config/termite/config-light &"

## download mp3 from youtube
alias ytmp3="youtube-dl --extract-audio --audio-format mp3"

## git clone depth 1
alias clone="git clone --depth 1"


shopt -s autocd # change to named directory
shopt -s cdspell # autocorrects cd misspellings
shopt -s cmdhist # save multi-line commands in history as single line
shopt -s histappend # do not overwrite history
shopt -s expand_aliases # expand aliases

#neofetch
EDITOR=nano
