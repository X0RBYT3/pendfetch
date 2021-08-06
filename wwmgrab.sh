#!/bin/sh
[ -z "$DISPLAY" ] && {
    exit 1
}

wm="$(xprop -root -notype _NET_WM_NAME)"
wm="${wm##*= \"}"
wm="${wm%%\"*}"

printf '%s\n' "$wm"
