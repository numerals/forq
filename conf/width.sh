#! /usr/bin/sh
expr "$(xrandr | head -n 2 | tail -n 1 | awk '{ print $4 }')" : '\(.*\)[x].*[+].*[+]'
# Can also be implemented as
# xrandr | head -n 1 | awk '{ print $8 }'
