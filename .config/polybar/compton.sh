#!/bin/sh

#The icon that would change color
icon=" "

if pgrep -x "compton" > /dev/null
then
	echo "%{F#D1D1D0}$icon"
else
	echo "%{F#000000}$icon"
fi
