## Left Prompt
function fish_prompt
    # Set the annoying greeting to empty
    set fish_greeting
    set -l last_status $status
    # Show the current working directory
    set_color black
    if test (id -u) -eq 0
		set_color --background=yellow
	else
		set_color --background=red
	end
    if test (id -u) -eq 0
        echo -n ' # '
    else
        echo -n ' $ '
    end
    set_color normal
    set_color --background=black
    echo -n ' '
    echo -n $USER
    echo -n ' '
    set_color normal
    echo -n ' '
end

## Right Prompt
function fish_right_prompt
    set_color --background=black
    echo -n ' '
    echo -n (prompt_pwd)
    echo -n ' '
    set_color black
    set_color --background=blue
    echo -n ' '
    echo -n (hostname -s)
	echo -n ' '
    set_color normal
end

## Window title
function fish_title
    echo -n 'fish in '
    prompt_pwd
end

        
## Coloring
set fish_color_autosuggestion black
set fish_color_command normal
set fish_color_comment black
set fish_color_cwd blue
set fish_color_cwd_root red
set fish_color_end magenta
set fish_color_error yellow
set fish_color_escape cyan
set fish_color_history_current cyan
set fish_color_host normal
set fish_color_match blue
set fish_color_normal normal
set fish_color_operator cyan
set fish_color_param blue
set fish_color_quote green
set fish_color_redirection blue
set fish_color_search_match --background=black
set fish_color_selection blue
set fish_color_status red
set fish_color_user red
set fish_pager_color_completion blue
set fish_pager_color_description yellow
set fish_pager_color_prefix cyan
set fish_pager_color_progress cyan

## Aliases
alias ls "ls --group-directories-first"
alias lsl "ls --group-directories-first -lh"
alias version "apt-cache show"
alias font-refresh "fc-cache -fv"
alias clone "git clone --depth 1"
alias merge "xrdb ~/.Xresources"
alias search "apt-cache search"
alias install "sudo apt-get install --no-install-recommends"
alias upgrade "sudo apt-get upgrade"
alias update "sudo apt-get update"
alias remove "sudo apt-get remove"
alias purge "sudo apt-get remove --purge"
alias clean "sudo apt-get clean"
alias autoclean "sudo apt-get autoclean"
alias autoremove "sudo apt-get autoremove"
alias reconfigure "sudo dpkg-reconfigure"
alias pkguser "apt-mark showmanual | sed 's#/.*##' | tr '\n' ' '"
alias pkglist "dpkg --get-selections | grep -v deinstall |\
sed s/\tinstall//g | sed s/\t//g | sed s/:amd64//g | tr '\n' ' '"

## Keybinding
set fish_key_bindings fish_default_key_bindings

## Only runs on TTY
## But I don't know why the TTY coloring does not work
if test $TERM = "linux"
    export PATH="$PATH:$HOME/.scripts"
    echo -en "\e]P0141c21" #black
    echo -en "\e]P8263640" #darkgrey
    echo -en "\e]P1d12f2c" #darkred
    echo -en "\e]P9fa3935" #red
    echo -en "\e]P2819400" #darkgreen
    echo -en "\e]PAa4bd00" #green
    echo -en "\e]P3b08500" #brown
    echo -en "\e]PBd9a400" #yellow
    echo -en "\e]P42587cc" #darkblue
    echo -en "\e]PC2ca2f5" #blue
    echo -en "\e]P5696ebf" #darkmagenta
    echo -en "\e]PD8086e8" #magenta
    echo -en "\e]P6289c93" #darkcyan
    echo -en "\e]PE33c5ba" #cyan
    echo -en "\e]P7bfbaac" #lightgrey
    echo -en "\e]PFfdf6e3" #white
    clear
end

