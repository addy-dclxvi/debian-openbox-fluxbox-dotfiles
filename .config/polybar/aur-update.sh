#!/bin/bash

if [[ `cower -u | wc -l` > "0" ]]; then
    termite --geometry=480x250 -e "packer -Syu"
fi

exit 0
