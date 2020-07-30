#!/bin/bash
opts='pt' #treasure + shops, equipment only

if [ ! "$1" ]; then
  echo "Usage: $0 rom-filename [options]"
  exit
fi

if [ $2 ]; then
  opts=$2
fi

./randomizer.py  "$1" $opts
