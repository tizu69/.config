#!/usr/bin/env bash

sink=@DEFAULT_AUDIO_SINK@

by=$1 # string like 5%+ or 5%-; literal MUTE
if [[ $by == "MUTE" ]]; then
    wpctl set-mute $sink toggle
else
    wpctl set-volume -l 1 $sink $by
fi

newvol="$(wpctl get-volume "$sink")" # e.g. "Volume: 0.25"
newvol="${newvol:8}" # remove "Volume: "
newvol=$(awk "BEGIN { print $newvol * 100 }") # multiply by 100

dunstify -h string:x-dunst-stack-tag:volume "volume" -h int:value:"$newvol"