#!/bin/sh

START="al-compositor --start"
STOP="al-compositor --stop"
if pgrep -x "compton" > /dev/null
then
	$STOP
else
	$START
fi
