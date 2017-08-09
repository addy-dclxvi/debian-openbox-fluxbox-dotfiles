#!/bin/bash

if [[ `checkupdates | wc -l` > "0" ]]; then
    termite --geometry=480x250 -e "sudo pacman -Syu"
fi

exit 0
