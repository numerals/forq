#! /usr/bin/sh
expr "$(id | awk '{ print $1 }')" : "uid=\(.*\)(.*)"
