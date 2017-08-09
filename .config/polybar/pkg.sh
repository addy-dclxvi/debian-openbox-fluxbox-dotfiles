#!/bin/bash

pac=$(checkupdates | wc -l)
aur=$(cower -u | wc -l)

check=$((pac + aur))
if [[ "$check" > "0" ]]
then
    echo "%{F#D1D1D0}  $pac %{F#D1D1D0}  $aur "
fi

exit 0
