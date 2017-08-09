#!/bin/bash

pkill polybar
polybar --config=/home/addy/.config/polybar/config bar1 &
polybar --config=/home/addy/.config/polybar/config bar2 &

exit 0
